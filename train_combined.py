import os
from ultralytics import YOLO

def train_hazard_detection():
    # Define model weights
    base_model = yolov8n.pt
    last_checkpoint = runs/detect/train/weights/last.pt
    
    # Check if a previous training session exists to resume (logic from moretrain.ipynb)
    if os.path.exists(last_checkpoint):
        print(Resuming training from last checkpoint...)
        model = YOLO(last_checkpoint)
        resume_training = True
    else:
        print(Starting new training session...)
        model = YOLO(base_model)
        resume_training = False

    # Training parameters based on paper (Epochs: 100, Batch: 16, Size: 224)
    model.train(
        data=hazard.yaml,
        epochs=100,
        imgsz=224,
        batch=16,
        patience=50,
        save=True,
        project=runs/detect,
        name=train,
        exist_ok=True,
        resume=resume_training
    )

if __name__ == __main__:
    train_hazard_detection()