# import os
# import random
# from pathlib import Path

# raw_images = Path("dataset/raw_images")   # যেখানে সব original images আছে
# dataset_dir = Path("dataset")
# train_ratio = 0.8  # 80% train, 20% val

# # Create folder structure
# for folder in ["images/train", "images/val", "labels/train", "labels/val"]:
#     os.makedirs(dataset_dir / folder, exist_ok=True)

# # Get all image files
# image_files = [f for f in raw_images.iterdir() if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]]
# random.shuffle(image_files)

# split_index = int(len(image_files) * train_ratio)
# train_images = image_files[:split_index]
# val_images = image_files[split_index:]

# # Function to copy image + create dummy label
# def process_images(img_list, img_folder, label_folder):
#     for img_path in img_list:
#         # Copy image
#         dest_img = dataset_dir / img_folder / img_path.name
#         dest_img.write_bytes(img_path.read_bytes())

#         # Create dummy label file (full image box)
#         label_path = dataset_dir / label_folder / (img_path.stem + ".txt")
#         with open(label_path, "w") as f:
#             f.write("0 0.5 0.5 1.0 1.0\n")  # class 0, full image

# # Process train & val
# process_images(train_images, "images/train", "labels/train")
# process_images(val_images, "images/val", "labels/val")

# # Create dataset.yaml
# yaml_path = dataset_dir / "dataset.yaml"
# with open(yaml_path, "w") as f:
#     f.write(f"""path: dataset
# train: images/train
# val: images/val

# nc: 1
# names: ["trapped"]
# """)

# print("✅ Dataset structure ready!")
# print(f"Train images: {len(train_images)}, Val images: {len(val_images)}")
# print(f"dataset.yaml created at: {yaml_path}")


import os
import shutil
import random
import yaml


dataset_dir = "dataset" 
raw_images_dir = os.path.join(dataset_dir, "raw_images")  
train_ratio = 0.8  
classes = {"normal": 0, "trapped": 1}  


image_dest = {
    "train": os.path.join(dataset_dir, "images", "train"),
    "val": os.path.join(dataset_dir, "images", "val")
}
label_dest = {
    "train": os.path.join(dataset_dir, "labels", "train"),
    "val": os.path.join(dataset_dir, "labels", "val")
}


for folder in list(image_dest.values()) + list(label_dest.values()):
    os.makedirs(folder, exist_ok=True)


all_images = []
for fname in os.listdir(raw_images_dir):
    if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        
        label_class = None
        if "trapped" in fname.lower():
            label_class = classes["trapped"]
        elif "normal" in fname.lower():
            label_class = classes["normal"]
        else:
            continue  

        all_images.append((fname, label_class))


random.shuffle(all_images)
split_idx = int(len(all_images) * train_ratio)
train_images = all_images[:split_idx]
val_images = all_images[split_idx:]


def process_split(image_list, split_type):
    for fname, cls in image_list:
        
        src_img = os.path.join(raw_images_dir, fname)
        dst_img = os.path.join(image_dest[split_type], fname)
        shutil.copy2(src_img, dst_img)

        label_file = os.path.splitext(fname)[0] + ".txt"
        dst_label = os.path.join(label_dest[split_type], label_file)
        with open(dst_label, "w") as f:
            f.write(f"{cls} 0.5 0.5 1 1\n")


process_split(train_images, "train")
process_split(val_images, "val")

print(f"Train images: {len(train_images)}, Val images: {len(val_images)}")
print("Images copied and labels created!")


dataset_yaml = {
    'path': dataset_dir,
    'train': 'images/train',
    'val': 'images/val',
    'nc': len(classes),
    'names': list(classes.keys())
}

yaml_path = os.path.join(dataset_dir, "dataset.yaml")
with open(yaml_path, "w") as f:
    yaml.dump(dataset_yaml, f)

print(f"dataset.yaml created at: {yaml_path}")