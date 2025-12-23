from ultralytics import YOLO
import sys

def export_to_onnx(weights_path):
    # Load the best trained model
    try:
        model = YOLO(weights_path)
        print(fModel loaded from {weights_path})
        
        # Export settings aligned with Unity Barracuda requirements
        # Opset 12 is recommended for Barracuda compatibility
        success = model.export(
            format=onnx,
            opset=12,
            simplify=True
        )
        
        if success:
            print(Export completed successfully.)
        else:
            print(Export failed.)
            
    except Exception as e:
        print(fError during export: {e})

if __name__ == __main__:
    # Default path to best weights
    best_weights = runs/detect/train/weights/best.pt
    export_to_onnx(best_weights)