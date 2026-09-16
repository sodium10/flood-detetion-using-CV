# check_labels.py
import os

# Dataset labels path
dataset_path = "dataset/labels"
splits = ["train", "val"]

# Allowed class indices
allowed_classes = [0, 1]

errors_found = False

for split in splits:
    folder = os.path.join(dataset_path, split)
    if not os.path.exists(folder):
        print(f"⚠️ Folder does not exist: {folder}")
        continue

    for label_file in os.listdir(folder):
        if not label_file.endswith(".txt"):
            continue

        file_path = os.path.join(folder, label_file)
        with open(file_path, "r") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            parts = line.strip().split()
            if len(parts) == 0:
                continue
            class_index = int(parts[0])
            if class_index not in allowed_classes:
                print(f"⚠️ Wrong class index in {file_path} line {i+1}: {class_index}")
                errors_found = True
            else:
                print(f"{file_path} line {i+1}: class {class_index}")

if not errors_found:
    print("\nAll labels are correct")
else:
    print("\nSome labels have wrong class indices ⚠️. Fix them before training.")