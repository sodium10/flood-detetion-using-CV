# from ultralytics import YOLO
# import cv2
# import os


# model = YOLO("runs/detect/train/weights/best.pt") 


# test_images_path = "dataset1/test_images"
# output_folder = "runs/detect/visual_debug_results"
# os.makedirs(output_folder, exist_ok=True)

# # 3. Prediction
# results = model.predict(
#     source=test_images_path,
#     conf=0.05,      
#     save=False,      
#     project=output_folder,
#     name="predict_visual"
# )


# for r in results:
#     img = r.orig_img.copy()  
#     if r.boxes.xyxy.shape[0] == 0:
#         print(f"No detections in image: {r.path}")
#     else:
#         print(f"\nImage: {r.path}")
#         for box, conf, cls in zip(r.boxes.xyxy, r.boxes.conf, r.boxes.cls):
#             x1, y1, x2, y2 = map(int, box.tolist())
#             label = f"Class:{int(cls.item())} Conf:{conf.item():.2f}"
#             print(f"  {label}, Box: {x1},{y1},{x2},{y2}")
            
#             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(img, label, (x1, y1 - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
#     cv2.imshow("Detection", img)
#     cv2.waitKey(0)  

    
#     save_path = os.path.join(output_folder, os.path.basename(r.path))
#     cv2.imwrite(save_path, img)

# cv2.destroyAllWindows()
# print(f"\nAll visual results saved in: {output_folder}")


from ultralytics import YOLO

model = YOLO("runs/detect/train2/weights/best.pt")

results = model.predict(
    source="dataset/valid/images",
    conf=0.2,
    save=True
)

for r in results:
    r.show()