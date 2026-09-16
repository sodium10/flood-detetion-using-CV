import os

# ছবির ডিরেক্টরি এবং লেবেল ডিরেক্টরি
image_dirs = {
    "normal": "dataset/normal_images",
    "trapped": "dataset/trapped_images"
}

label_dirs = {
    "normal": "labels/normal_images",
    "trapped": "labels/trapped_images"
}

# যদি লেবেল ডিরেক্টরি না থাকে, তৈরি করে দাও
for dir_path in label_dirs.values():
    os.makedirs(dir_path, exist_ok=True)

# লেবেল জেনারেট করা
for class_name, img_dir in image_dirs.items():
    lbl_dir = label_dirs[class_name]
    images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

    for img_file in images:
        # লেবেল ফাইলের নাম একই
        base_name = os.path.splitext(img_file)[0]
        label_file = os.path.join(lbl_dir, f"{base_name}.txt")

        # ডামি লেবেল: class_id x_center y_center width height (YOLO format)
        # এখানে x_center, y_center, width, height 0.5 দিয়ে ডামি তৈরি করা হলো
        class_id = 0 if class_name == "normal" else 1
        with open(label_file, "w") as f:
            f.write(f"{class_id} 0.5 0.5 0.5 0.5\n")

print("Labels generated successfully!")