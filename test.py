from ultralytics import YOLO
import os
import json
import torch

# -------------------------------
# Device selection (Mac M2 GPU)
# -------------------------------
if torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(f"Using device: {device}")

# -------------------------------
# Paths
# -------------------------------
model_path = "runs/detect/Disaster_30EPOCH/weights/best.pt"
test_folder = "temp.v5-dataset.yolov12/test/images"
output_json = "test_results.json"

# -------------------------------
# Load model
# -------------------------------
model = YOLO(model_path)

all_results = []

# -------------------------------
# Run inference on test images
# -------------------------------
for img_name in sorted(os.listdir(test_folder)):

    if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img_path = os.path.join(test_folder, img_name)

    results = model(
        img_path,
        conf=0.25,
        device=device,
        verbose=False
    )

    for r in results:
        if not r.boxes:
            continue
        image_result = {
        "image_name": img_name,
        "total_detections": 0,
        "category_count": {name: 0 for name in model.names.values()},
        "detections": []
    }

    boxes = r.boxes

    if boxes is not None and len(boxes) > 0:

        for box in boxes:

            cls_id = int(box.cls[0])
            category = model.names[cls_id]
            confidence = float(box.conf[0])

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            image_result["detections"].append({
                "category": category,
                "confidence": round(confidence, 4),
                "bbox": [
                    round(x1, 2),
                    round(y1, 2),
                    round(x2, 2),
                    round(y2, 2)
                ]
            })

            # Increment category count
            image_result["category_count"][category] += 1

    image_result["total_detections"] = len(image_result["detections"])

    all_results.append(image_result)

# -------------------------------
# Save JSON
# -------------------------------
with open(output_json, "w") as f:
    json.dump(all_results, f, indent=4)

print("\nTest completed successfully!")
print(f"Results saved to: {output_json}")
print(f"Total images processed: {len(all_results)}")