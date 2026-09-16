import cv2
import os
from ultralytics import YOLO

# Load model
model = YOLO("runs/detect/train/weights/best.pt")

# Run prediction
results = model.predict(source="dataset1/test_images", save=False)

output_folder = "runs/detect/visual_debug"
os.makedirs(output_folder, exist_ok=True)

for r in results:
    img = r.orig_img.copy()
    if r.boxes.xyxy.shape[0] > 0:
        for box, conf, cls in zip(r.boxes.xyxy, r.boxes.conf, r.boxes.cls):
            x1, y1, x2, y2 = map(int, box.tolist())
            label = f"Class:{int(cls.item())} Conf:{conf.item():.2f}"
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(img, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    save_path = os.path.join(output_folder, os.path.basename(r.path))
    cv2.imwrite(save_path, img)