import os
from CONFIG import *
import shutil
import fileinput
import re
from copy import deepcopy
from PIL import Image
from math import floor, ceil

LOCAL_IMAGE_COUNTER = deepcopy(IMAGE_COUNTER)

def get_file_paths(path=f"{os.getcwd()}/diceImages"):
    print("Getting file paths...")
    files = []
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(path)):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if not file_path.endswith('.directory') and file not in (".gitignore", 'class_list.txt'):
                files.append(file_path)
    return files


def get_object_files(path=f"{os.getcwd()}/diceImages"):
    file_objects = dict()
    for dirpath, dirnames, filenames in os.walk(os.path.abspath(path)):
        for file in filenames:
            if not file.endswith('.directory') and file not in (".gitignore", 'class_list.txt'):

                file_path = os.path.join(dirpath, file)
                file_name_raw, extension = file.split('.')

                if file_name_raw not in file_objects:
                    file_objects[file_name_raw] = dict()

                file_objects[file_name_raw]['group'] = get_group(file_path)
                file_objects[file_name_raw]['die'] = get_die(file_path)

                if extension in ['txt']:
                    file_objects[file_name_raw]['txt_src'] = file_path
                    file_objects[file_name_raw]['txt_dst'] = f"{os.getcwd()}/dataset/dice/{file_objects[file_name_raw]['group']}/{file}"
                elif extension in IMAGE_EXTENSIONS:
                    file_objects[file_name_raw]['img_src'] = file_path
                    file_objects[file_name_raw]['img_dst'] = f"{os.getcwd()}/dataset/dice/{file_objects[file_name_raw]['group']}/{file}"

    return file_objects


def get_group(file_path):
    group = 'test' if "/mixed/" in file_path else 'train'
    return group


def get_die(file_path):
    for die in DIES.keys():
        if f"/{die}/" in file_path:
            return die


def copy_new_files(file_objects):
    for item_name, item_info in file_objects.items():
        try:
            os.makedirs(os.path.dirname(item_info['txt_dst']), exist_ok=True)
            shutil.copy(item_info['txt_src'], item_info['txt_dst'])
        except KeyError as e:
            print(f"Missing txt for {item_info['img_src']}")
        try:
            #if not os.path.exists(item_info['img_dst']):
            os.makedirs(os.path.dirname(item_info['img_dst']), exist_ok=True)
            shutil.copy(item_info['img_src'], item_info['img_dst'])
        except KeyError as e:
            print(f"Missing img for {item_info['txt_src']}")


def remap_classes(file_objects):
    txt_paths = []
    for item_info in file_objects.values():
        try:
            txt_paths.append(item_info['txt_dst'])
        except KeyError:
            pass

    for line in fileinput.input(txt_paths, inplace=1):
        id = re.findall('^(\S+)', line)
        id = int(id[0])
        for dice_class in CLASS_ID_MAPPING:
            if dice_class[SOURCE_ID] == id:
                new_id = dice_class[DICE_ID]
        line = re.sub(f'^{id}\s', f'{new_id} ', line.rstrip())
        print(line)


def generate_image_lists(file_objects):
    train = []
    test = []

    for file_object in file_objects.values():
        darket_path = f"data/{DARKNET_OBJ_NAME}/{os.path.basename(file_object['img_dst'])}"
        if file_object['group'] == 'test':
            test.append(darket_path + '\n')
        else:
            train.append(darket_path + '\n')

    with open('./dataset/dice/train.txt', 'w') as f:
        f.writelines(train)

    with open('./dataset/dice/test.txt', 'w') as f:
        f.writelines(test)


def get_yolo_objects(lines: list):
    """
    given a list of str lines of text from a single yolo .txt returns a list of dicts containing
    properties of each .txt
    """
    object_template = {SOURCE_ID: 0, POSITION_X: 0.0, POSITION_Y: 0.0, WIDTH_X: 0.0, HEIGHT_Y: 0.0}
    yolo_objects = list()
    for line in lines:
        items = line.split()
        yolo_object = deepcopy(object_template)
        yolo_object[SOURCE_ID] = int(items[0])
        yolo_object[POSITION_X] = float(items[1])
        yolo_object[POSITION_Y] = float(items[2])
        yolo_object[WIDTH_X] = float(items[3])
        yolo_object[HEIGHT_Y] = float(items[4])
        yolo_objects.append(yolo_object)

    return yolo_objects


def get_cropped_images(image: Image, yolo_objects: list):
    """
    given an image, list of yolo objects obtained from get_yolo_objects() method returns  a list of
    dicts containing for each bounding box the source_id and touple used for cropping(Image.crop(touple()))
    """
    image_template = {SOURCE_ID: 0, CROPPED_IMG: None}
    original_width, original_height = image.size
    print(f"width={original_width}, height={original_height}")
    images = list()
    for yolo_object in yolo_objects:
        left = (yolo_object[POSITION_X] - 0.5 * yolo_object[WIDTH_X]) * original_width
        top = (yolo_object[POSITION_Y] + 0.5 * yolo_object[HEIGHT_Y]) * original_height
        right = (yolo_object[POSITION_X] + 0.5 * yolo_object[WIDTH_X]) * original_width
        bottom = (yolo_object[POSITION_Y] - 0.5 * yolo_object[HEIGHT_Y]) * original_height

        image_object = deepcopy(image_template)
        crop_touple = (ceil(left), floor(top), floor(right), ceil(bottom))
        print(crop_touple)

        image_object[SOURCE_ID] = yolo_object[SOURCE_ID]
        image_object[CROPPED_IMG] = image.crop(crop_touple)
        image_object[CROPPED_IMG].show()
        images.append(image_object)
        exit(0)

    image.show()
    exit(0)

    return images


def write_classifier_images(die: str, group: str, image_objects: list):
    print(f"Writing classifier images...")
    for image_object in image_objects:
        img_number = LOCAL_IMAGE_COUNTER[die][group]
        LOCAL_IMAGE_COUNTER[die][group] += 1
        for number_id in CLASS_ID_MAPPING:
            if number_id[SOURCE_ID] == image_object[SOURCE_ID]:
                die_number_id = number_id[NUMBERS_ID]
                break

        save_path = f"./dataset/numbers/{die}/{group}/{img_number}_{die_number_id}.jpg"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        image_object[CROPPED_IMG].save(save_path)


def get_classifier_images(file_objects: dict):
    for file_name_raw, file_object in file_objects.items():
        txt_src = file_object['txt_src']
        img_src = file_object['img_src']
        with open(txt_src) as file:
            text = file.readlines()
        lines = [line.rstrip('\n') for line in text]
        yolo_objects = get_yolo_objects(lines)
        image = Image.open(img_src)
        image_objects = get_cropped_images(image, yolo_objects)
        die = get_die(txt_src)
        group = get_group(txt_src)
        write_classifier_images(die, group, image_objects)


if __name__ == '__main__':

    of = get_object_files()
    '''
    copy_new_files(of)
    remap_classes(of)
    generate_image_lists(of)
    '''
    get_classifier_images(of)




