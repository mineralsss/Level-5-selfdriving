import numpy as np
import supervision as sv
import torch
from ultralytics import YOLO
import cv2
import os
import random
os.environ['KMP_DUPLICATE_LIB_OK']='True'

#global variable
directory = r'C:\Users\tuana\Documents\frames'
device = "cuda:0"
model = YOLO(r"C:\Users\tuana\Documents\Models\yolov9c.engine")
#
class Image:
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(directory, self.name)
        self.as_array = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)

    @staticmethod
    def random_images():
        images = []
        image_files = os.listdir(directory)
        random_image_file = random.sample(image_files, 1)
        for image in random_image_file:
            tmp = cv2.imread(os.path.join(directory, image))
            images.append(cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB))
        return images


    @staticmethod
    def get_detection(image):
        coi = [0, 1, 2, 3, 5, 6, 7, 8, 9, 11]
        result = model.predict(image, classes = coi, conf = 0.45)
        return result
class Midas:

    def __init__(self):
        self.model_type = "DPT_Hybrid"
        self.midas = torch.hub.load("intel-isl/MiDaS", self.model_type)
        self.midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
        self.device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        self.image = None

    def get_depth_map(self, image_path):
        self.midas.to(self.device)
        self.midas.eval()
        if self.model_type == "DPT_Large" or self.model_type == "DPT_Hybrid":
            transform = self.midas_transforms.dpt_transform
        else:
            transform = self.midas_transforms.small_transform
        input_batch = transform(image_path).to(self.device)
        with torch.no_grad():
            prediction = self.midas(input_batch)

            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=img.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()

        output = prediction.cpu().numpy()
        return output

img = Image.random_images()[0]
'''while True:
    img = Image.random_images()[0]
    midas = Midas()
    box_annotator = sv.BoxAnnotator(thickness= 4, text_thickness= 4, text_scale= 2)
    for r in Image.get_detection(img):
        detections = sv.Detections(
            xyxy = r.boxes.xyxy.cpu().numpy(),
            confidence = r.boxes.conf.cpu().numpy(),
            class_id = r.boxes.cls.cpu().numpy().astype(int)
        )
        frame = box_annotator.annotate(midas.get_depth_map(img), detections = detections)
        sv.plot_image(frame)
'''

#testing changes
blured_img = img[177:466+177, 477:1276+477].copy()
blured_img = cv2.GaussianBlur(blured_img,(5,5),  0)
edge = cv2.Canny(blured_img, 100, 120)
sv.plot_image(img)
sv.plot_image(edge)