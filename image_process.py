from ultralytics import YOLO
import torch
torch.cuda.set_device(1)
model = YOLO("yolov8.yaml", device = "gpu")