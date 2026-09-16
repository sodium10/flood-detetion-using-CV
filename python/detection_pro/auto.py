import os

# Paths
dataset_path = "dataset"

# YOLO full-image box
BOX = "0.5 0.5 1.0 1.0"

# Process raw images (no train/val split for this dataset)
img_dir = os.path.join(dataset_path, "raw_images")
label_dir = os.path.join(dataset_path, "labels", "train")
os.makedirs(label_dir, exist_ok=True)

for img in os.listdir(img_dir):
    if not img.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img_name = os.path.splitext(img)[0]

    # Class detect from filename
    if "trapped" in img.lower():
        class_id = 1
    elif "normal" in img.lower():
        class_id = 0
    else:
        print(f"⚠️ Skipping unknown image: {img}")
        continue

    label_path = os.path.join(label_dir, img_name + ".txt")

    with open(label_path, "w") as f:
        f.write(f"{class_id} {BOX}\n")

print("Auto annotation completed (full-image boxes)")