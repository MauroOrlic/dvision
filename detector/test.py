import cv2
import argparse
from detector.darknet_detector import DarknetDetector
from detector.CONFIG import DICE_CFG, DICE_NAMES, DICE_WEIGHTS

if __name__ == '__main__':
    '''
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-i', '--image', required=True)
    arguments = vars(argument_parser.parse_args())
    '''
    image_path = "/home/mauro/Workspace/dvision/detector/test.jpg"
    dice_detector = DarknetDetector(DICE_CFG, DICE_WEIGHTS, minimum_confidence=0.01)
    image = cv2.imread(image_path)
    boxes = dice_detector.process_image(image)
    for box in boxes:
        print(box)

