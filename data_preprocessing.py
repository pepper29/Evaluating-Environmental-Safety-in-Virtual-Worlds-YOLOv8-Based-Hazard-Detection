import os
import cv2
import glob

def preprocess_images(source_dir, dest_dir, sizes):
    # Create destination directories if they do not exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get all image files
    image_paths = glob.glob(os.path.join(source_dir, *.jpg))
    
    for img_path in image_paths:
        filename = os.path.basename(img_path)
        img = cv2.imread(img_path)
        
        if img is None:
            continue
            
        # Resize for each target size defined in the paper
        for size in sizes:
            # Create sub-directory for each size
            size_dir = os.path.join(dest_dir, str(size))
            if not os.path.exists(size_dir):
                os.makedirs(size_dir)
                
            resized_img = cv2.resize(img, (size, size))
            save_path = os.path.join(size_dir, filename)
            cv2.imwrite(save_path, resized_img)
            print(fProcessed {filename} to size {size})

# Configuration
# source_path = dataset/raw_images
# destination_path = dataset/preprocessed
# target_sizes = [160, 224, 320, 480, 640]
if __name__ == __main__:
    preprocess_images(dataset/raw, dataset/processed, [160, 224, 320, 480, 640])