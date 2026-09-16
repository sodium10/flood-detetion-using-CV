# train_model.py
from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt") 


dataset_path = "dataset"


supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.webp', '.heic')


def filter_images(folder):
    for file in os.listdir(folder):
        if not file.lower().endswith(supported_formats):
            print(f"Ignoring unsupported file: {file}")
            os.remove(os.path.join(folder, file)) 


filter_images(os.path.join(dataset_path, "images/train"))
filter_images(os.path.join(dataset_path, "images/val"))


model.train(
    data=os.path.join(dataset_path, "dataset.yaml"),  
    epochs=10,       
    imgsz=640,
    batch=16,
    device='cpu',  
    exist_ok=True
)

# from ultralytics import YOLO

# model = YOLO("yolov8n.pt")

# model.train(
#     data="dataset/data.yaml",
#     epochs=20,
#     imgsz=640,
#     batch=16,
#     device="cpu"
# )