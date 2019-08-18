import cv2
import numpy


class DarknetDetector:
    def __init__(self, path_names:str, path_cfg:str, path_weights:str, minimum_confidence=0.5, nms_threshold=0.3):
        self.class_names = self._get_classes(path_names)
        self.darknet = cv2.dnn.readNetFromDarknet(path_cfg, path_weights)
        self.layer_names = self._get_layer_names(self.darknet)
        self.minimum_confidence = minimum_confidence
        self.nms_threshold = nms_threshold

    def process_image(self, image):
        image_height, image_width = image.shape[:2]
        blob = self._get_blob_from_image(image)
        self.darknet.setInput(blob)
        layer_outputs = self.darknet.forward(self.layer_names)
        detected_objects = self._process_layer_outputs(layer_outputs, image_height, image_width)
        return detected_objects

    @staticmethod
    def _get_layer_names(net):
        layer_names = net.getLayerNames()
        layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        return layer_names

    @staticmethod
    def _get_classes(path_names):
        with open(path_names) as names_file:
            text = names_file.read()
            class_names = text.strip().split('\n')
        return class_names

    @staticmethod
    def _get_blob_from_image(image):
        blob = cv2.dnn.blobFromImage(image, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)
        return blob

    @staticmethod
    def _convert_bounding_box_format(yolo_bounding_box: list, image_height, image_width):
        new_box = yolo_bounding_box * numpy.array([image_width, image_height, image_width, image_height])
        center_x, center_y, width, height = new_box.astype('int')
        top_left_x = int(center_x - (width / 2.0))
        top_left_y = int(center_y - (height / 2.0))
        return [top_left_x, top_left_y, int(width), int(height)]

    def _process_layer_outputs(self, layer_outputs, image_height, image_width):
        class_ids = []
        bounding_boxes = []
        confidences = []

        for output in layer_outputs:
            for detection in output:

                scores = detection[5:]
                class_id = numpy.argmax(scores)

                confidence = float(scores[class_id])
                if confidence > self.minimum_confidence:

                    bounding_box = self._convert_bounding_box_format(detection[0:4], image_height, image_width)

                    class_ids.append(class_id)
                    bounding_boxes.append(bounding_box)
                    confidences.append(confidence)

        idxs = cv2.dnn.NMSBoxes(bounding_boxes, confidences, self.minimum_confidence, self.nms_threshold)

        detected_objects = []
        for i in idxs.flatten():
            class_id = class_ids[i]
            bounding_box = (bounding_boxes[i][0], bounding_boxes[i][1], bounding_boxes[i][2], bounding_boxes[i][3])
            confidence = confidences[i]
            detected_objects.append((class_id, bounding_box, confidence))

        return detected_objects
