# Flood and Disaster Detection using Computer Vision (YOLOv12)

An intelligent computer vision system for real-time flood monitoring, risk assessment, and rescue victim detection using **YOLOv12**. This project detects flood hazard levels and trapped individuals to assist emergency rescue operations.

---

## 📌 Project Overview

- **Model Architecture**: YOLOv12 nano (`yolo12n.pt`)
- **Acceleration**: Apple Silicon GPU (MPS) / CUDA / CPU
- **Dataset**: Custom annotated disaster dataset from Roboflow Universe
- **Key Detection Classes**:
  1. `critical risk`
  2. `high risk`
  3. `medium risk`
  4. `low risk`
  5. `rescue individual`

---

## 📊 Training Results & Performance

Trained for **30 Epochs**:
- **mAP@50**: ~90.9%
- **Precision**: ~87.2%
- **Recall**: ~86.8%

Visualizations including confusion matrices, PR curves, F1 curves, and training batch predictions are saved under [`runs/detect/Disaster_30EPOCH/`](runs/detect/Disaster_30EPOCH/).

---

## 📂 Project Structure

```
├── train.py                                # Training pipeline using YOLOv12
├── test.py                                 # Evaluation and inference script producing structured JSON
├── requirements.txt                        # Required Python packages
├── test_results.json                       # Sample test set inference results
├── yolo12n.pt                              # YOLOv12 nano base model weights
├── runs/
│   └── detect/Disaster_30EPOCH/            # Training logs, validation metrics, and weights
│       ├── weights/
│       │   ├── best.pt                     # Best fine-tuned model checkpoint
│       │   └── last.pt                     # Last checkpoint
│       ├── results.png                     # Loss and metric curves
│       ├── confusion_matrix.png            # Confusion matrix
│       └── ...
└── temp.v5-dataset.yolov12/
    ├── data.yaml                           # Dataset class and path configurations
    └── README.roboflow.txt                 # Dataset metadata and Roboflow details
```

---

## 🚀 Getting Started

### 1. Installation

Clone this repository and install the dependencies:

```bash
git clone https://github.com/sodium10/flood-detetion-using-CV.git
cd flood-detetion-using-CV
pip install -r requirements.txt
```

### 2. Dataset

The dataset configuration is available in `temp.v5-dataset.yolov12/data.yaml`.
You can download or export the dataset directly from [Roboflow Universe](https://universe.roboflow.com/resqtech/temp-negz4/dataset/5).

### 3. Training

Run the training script (configured by default for Apple Silicon GPU with `device="mps"`):

```bash
python train.py
```

### 4. Evaluation & Testing

Run inference on test images using the best trained weights (`runs/detect/Disaster_30EPOCH/weights/best.pt`):

```bash
python test.py
```

Detections and category statistics will be exported to `test_results.json`.

---

## 📜 License

This project and its associated dataset are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
