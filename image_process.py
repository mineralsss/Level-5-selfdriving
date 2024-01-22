from ultralytics import YOLO
import torch
torch.cuda.set_device(0)
model = YOLO("yolov8n.yaml")
if __name__ == "__main__":
    result = model.train(data = r"C:\Users\tuana\Downloads\archive\test\data.yaml", epochs = 3, device = "0")