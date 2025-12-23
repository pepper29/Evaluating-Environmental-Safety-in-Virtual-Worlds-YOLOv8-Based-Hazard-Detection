from ultralytics import YOLO

def evaluate_model(weights_path):
    # Load the trained model
    model = YOLO(weights_path)
    
    # Validate on the test/val set defined in yaml
    metrics = model.val(imgsz=224, batch=16)
    
    # Extract specific metrics cited in the paper
    precision = metrics.box.p
    recall = metrics.box.r
    map50 = metrics.box.map50
    map50_95 = metrics.box.map
    
    # F1 Score calculation: 2 * (P * R) / (P + R)
    # Note: Ultralytics metrics object may perform this internally, 
    # but manual calculation ensures clarity based on the paper formula (Eq 1).
    if (precision + recall) > 0:
        f1 = 2 * (precision * recall) / (precision + recall)
    else:
        f1 = 0
        
    print(--- Performance Metrics ---)
    print(fPrecision: {precision:.3f})
    print(fRecall: {recall:.3f})
    print(fmAP@50: {map50:.3f})
    print(fmAP@50-95: {map50_95:.3f})
    print(fF1 Score: {f1:.3f})

if __name__ == __main__:
    evaluate_model(runs/detect/train/weights/best.pt)