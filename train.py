from ultralytics import YOLO

# Use Apple GPU
device = "mps"

data_yaml = "temp.v5-dataset.yolov12/data.yaml"

model = YOLO("yolo12n.pt")

results = model.train(
    data=data_yaml,
    epochs=30,
    patience=5,
    imgsz=640,
    batch=10,
    device=device,
    name="Disaster_30EPOCH"
)