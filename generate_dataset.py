import os
from CONFIG import *
import shutil
import fileinput
import re


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
                    file_objects[file_name_raw]['txt_dst'] = f"{os.getcwd()}/generated_dataset/{file_objects[file_name_raw]['group']}/{file}"
                elif extension in ['JPG', 'JPEG', 'jpg', 'jpeg']:
                    file_objects[file_name_raw]['img_src'] = file_path
                    file_objects[file_name_raw]['img_dst'] = f"{os.getcwd()}/generated_dataset/{file_objects[file_name_raw]['group']}/{file}"

    return file_objects


def get_group(file_path):
    group = 'test' if "/mixed/" in file_path else 'train'
    return group


def get_die(file_path):
    for die in DIES:
        if f"/{die}/" in file_path:
            return die


def copy_new_files(file_objects):
    for item_name, item_info in file_objects.items():
        try:
            shutil.copy(item_info['txt_src'], item_info['txt_dst'])
        except KeyError as e:
            print(f"Missing txt for {item_info['img_src']}")
        try:
            if not os.path.exists(item_info['img_dst']):
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

    with open('./generated_dataset/train.txt', 'w') as f:
        f.writelines(train)

    with open('./generated_dataset/test.txt', 'w') as f:
        f.writelines(test)

if __name__ == '__main__':

    of = get_object_files()
    copy_new_files(of)
    remap_classes(of)
    generate_image_lists(of)

