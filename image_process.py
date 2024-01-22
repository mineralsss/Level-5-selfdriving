from ultralytics import YOLO
import cv2
def tracking():
    model = YOLO(r"c:\Users\tuana\Downloads\yolov8m.pt")
    result = model.track(source = "Euro Truck Simulator 2 1_19_2024 10_12_02 AM.png", show = True, tracker = "bytetrack.yaml")
    cv2.waitKey(0)
tracking()