# Script to convert yolo annotations to voc format

# Sample format
# <annotation>
#     <folder>_image_fashion</folder>
#     <filename>brooke-cagle-39574.jpg</filename>
#     <size>
#         <width>1200</width>
#         <height>800</height>
#         <depth>3</depth>
#     </size>
#     <segmented>0</segmented>
#     <object>
#         <name>head</name>
#         <pose>Unspecified</pose>
#         <truncated>0</truncated>
#         <difficult>0</difficult>
#         <bndbox>
#             <xmin>549</xmin>
#             <ymin>251</ymin>
#             <xmax>625</xmax>
#             <ymax>335</ymax>
#         </bndbox>
#     </object>
# <annotation>
import os
import xml.etree.cElementTree as ET
from PIL import Image

ANNOTATIONS_DIR_PREFIX = "annotations"

DESTINATION_DIR = "converted_labels"

CLASS_MAPPING = {
        '0':'d4_1',
        '1':'d4_2',
        '2':'d4_3',
        '3':'d4_4',
        '4':'d6_1',
        '5':'d6_2',
        '6':'d6_3',
        '7':'d6_4',
        '8':'d6_5',
        '9':'d6_6',
        '10':'d8_1',
        '11':'d8_2',
        '12':'d8_3',
        '13':'d8_4',
        '14':'d8_5',
        '15':'d8_6',
        '16':'d8_7',
        '17':'d8_8',
        '18':'d10_1',
        '19':'d10_2',
        '20':'d10_3',
        '21':'d10_4',
        '22':'d10_5',
        '23':'d10_6',
        '24':'d10_7',
        '25':'d10_8',
        '26':'d10_9',
        '27':'d10_10',
        '28':'d12_1',
        '29':'d12_2',
        '30':'d12_3',
        '31':'d12_4',
        '32':'d12_5',
        '33':'d12_6',
        '34':'d12_7',
        '35':'d12_8',
        '36':'d12_9',
        '37':'d12_10',
        '38':'d12_11',
        '39':'d12_12',
        '40':'d20_1',
        '41':'d20_2',
        '42':'d20_3',
        '43':'d20_4',
        '44':'d20_5',
        '45':'d20_6',
        '46':'d20_7',
        '47':'d20_8',
        '48':'d20_9',
        '49':'d20_10',
        '50':'d20_11',
        '51':'d20_12',
        '52':'d20_13',
        '53':'d20_14',
        '54':'d20_15',
        '55':'d20_16',
        '56':'d20_17',
        '57':'d20_18',
        '58':'d20_19',
        '59':'d20_20',
        '60':'d100_00',
        '61':'d100_10',
        '62':'d100_20',
        '63':'d100_30',
        '64':'d100_40',
        '65':'d100_50',
        '66':'d100_60',
        '67':'d100_70',
        '68':'d100_80',
        '69':'d100_90'
        }


def create_root(file_prefix, width, height):
    root = ET.Element("annotations")
    ET.SubElement(root, "filename").text = "{}.jpg".format(file_prefix)
    ET.SubElement(root, "folder").text = "images"
    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(width)
    ET.SubElement(size, "height").text = str(height)
    ET.SubElement(size, "depth").text = "3"
    return root


def create_object_annotation(root, voc_labels):
    for voc_label in voc_labels:
        obj = ET.SubElement(root, "object")
        ET.SubElement(obj, "name").text = voc_label[0]
        ET.SubElement(obj, "pose").text = "Unspecified"
        ET.SubElement(obj, "truncated").text = str(0)
        ET.SubElement(obj, "difficult").text = str(0)
        bbox = ET.SubElement(obj, "bndbox")
        ET.SubElement(bbox, "xmin").text = str(voc_label[1])
        ET.SubElement(bbox, "ymin").text = str(voc_label[2])
        ET.SubElement(bbox, "xmax").text = str(voc_label[3])
        ET.SubElement(bbox, "ymax").text = str(voc_label[4])
    return root


def create_file(file_prefix, width, height, voc_labels):
    root = create_root(file_prefix, width, height)
    root = create_object_annotation(root, voc_labels)
    tree = ET.ElementTree(root)
    tree.write("{}/{}.xml".format(DESTINATION_DIR, file_prefix))


def read_file(file_path):
    file_prefix = file_path.split(".txt")[0]
    image_file_name = "{}.jpg".format(file_prefix)
    img = Image.open("{}/{}".format("images", image_file_name))
    w, h = img.size
    with open(file_path, 'r') as file:
        lines = file.readlines()
        voc_labels = []
        for line in lines:
            voc = []
            line = line.strip()
            data = line.split()
            voc.append(CLASS_MAPPING.get(data[0]))
            bbox_width = float(data[3]) * w
            bbox_height = float(data[4]) * h
            center_x = float(data[1]) * w
            center_y = float(data[2]) * h
            voc.append(int(center_x - (bbox_width / 2)))
            voc.append(int(center_y - (bbox_height / 2)))
            voc.append(int(center_x + (bbox_width / 2)))
            voc.append(int(center_y + (bbox_height / 2)))
            voc_labels.append(voc)
        create_file(file_prefix, w, h, voc_labels)
    print("Processing complete for file: {}".format(file_path))


def start(dir_name):
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)
    for filename in os.listdir(ANNOTATIONS_DIR_PREFIX):
        if filename.endswith('txt'):
            read_file(filename)
        else:
            print("Skipping file: {}".format(filename))


if __name__ == "__main__":
    """
    Create images and annotations directories, put images in images dir and yolo *.txt in annotation directory, run this script with argument '.'
    """
    import sys
    start(sys.argv[0]) 
