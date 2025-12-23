import time
import torch
import numpy as np
from ultralytics import YOLO

def benchmark_speed(weights_path, test_image_path):
    model = YOLO(weights_path)
    
    # Image sizes used in the experiment
    sizes = [160, 224, 320, 480, 640]
    
    print(--- Inference Time Benchmark ---)
    
    # Warmup to stabilize GPU/CPU
    print(Warming up...)
    model.predict(test_image_path, imgsz=224, verbose=False)
    
    for size in sizes:
        # Measure inference time over multiple runs for stability
        times = []
        for _ in range(10):
            start = time.time()
            model.predict(test_image_path, imgsz=size, verbose=False)
            end = time.time()
            times.append((end - start) * 1000) # Convert to ms
            
        avg_time = np.mean(times)
        print(fImage Size: {size}x{size} | Average Time: {avg_time:.2f} ms)

if __name__ == __main__:
    # Ensure a sample image exists for testing
    benchmark_speed(runs/detect/train/weights/best.pt, dataset/test/sample.jpg)