import os
from pathlib import Path
import numpy as np
from PIL import Image, features
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
import time
import psutil
import gc
from tqdm import tqdm

# Check for WebP support
if features.check('webp'):
    print("WebP support is enabled")
else:
    print("Warning: WebP support not found. Please upgrade Pillow:")
    print("pip install --upgrade Pillow")

# Nord color palette
NORD_COLORS = [
    (46, 52, 64),   # nord0: Polar Night
    (59, 66, 82),   # nord1
    (67, 76, 94),   # nord2
    (76, 86, 106),  # nord3
    (216, 222, 233),# nord4: Snow Storm
    (229, 233, 240),# nord5
    (236, 239, 244),# nord6
    (143, 188, 187),# nord7: Frost
    (136, 192, 208),# nord8
    (129, 161, 193),# nord9
    (94, 129, 172), # nord10
    (191, 97, 106), # nord11: Aurora
    (208, 135, 112),# nord12
    (235, 203, 139),# nord13
    (163, 190, 140),# nord14
    (180, 142, 173) # nord15
]

# Convert NORD_COLORS to numpy array for faster processing
NORD_COLORS_ARRAY = np.array(NORD_COLORS)

def find_closest_nord_color_vectorized(pixels: np.ndarray) -> np.ndarray:
    """Vectorized version of finding closest Nord color."""
    # Reshape pixels to (n, 1, 3) and NORD_COLORS to (1, m, 3)
    pixels_reshaped = pixels.reshape(-1, 1, 3)
    nord_colors_reshaped = NORD_COLORS_ARRAY.reshape(1, -1, 3)
    
    # Calculate distances using broadcasting
    distances = np.sum((pixels_reshaped - nord_colors_reshaped) ** 2, axis=2)
    
    # Find indices of minimum distances
    closest_color_indices = np.argmin(distances, axis=1)
    
    # Return the closest colors
    return NORD_COLORS_ARRAY[closest_color_indices]

def get_chunk_size(image_size: tuple) -> int:
    """Determine optimal chunk size based on available memory."""
    available_memory = psutil.virtual_memory().available
    # Use 20% of available memory
    target_memory = available_memory * 0.2
    pixels_possible = target_memory // (3 * 4)  # 3 channels, 4 bytes per float
    return min(int(pixels_possible), 100000)

def process_image(image_path: Path, output_dir: Path, pbar: tqdm) -> None:
    """Process a single image and save its Nord version."""
    try:
        with Image.open(image_path) as img:
            # Handle transparency
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                img = img.convert('RGBA')
                background = Image.new('RGBA', img.size, (255, 255, 255, 255))
                img = Image.alpha_composite(background, img)
            
            img = img.convert('RGB')
            width, height = img.size
            
            # Convert to numpy array
            img_array = np.array(img)
            
            # Process in chunks to manage memory
            chunk_size = get_chunk_size(img.size)
            pixels = img_array.reshape(-1, 3)
            output_pixels = np.zeros_like(pixels)
            
            for i in range(0, len(pixels), chunk_size):
                chunk = pixels[i:i + chunk_size]
                output_pixels[i:i + chunk_size] = find_closest_nord_color_vectorized(chunk)
                
                # Force garbage collection after each chunk
                gc.collect()
            
            # Reshape back and create image
            output_array = output_pixels.reshape(height, width, 3)
            output_image = Image.fromarray(output_array.astype('uint8'))
            
            # Save with appropriate format
            output_format = image_path.suffix.lower()
            if output_format == '.webp':
                output_path = output_dir / f"nord_{image_path.stem}.webp"
                output_image.save(output_path, 'WEBP', quality=95, lossless=True)
            else:
                output_path = output_dir / f"nord_{image_path.name}"
                output_image.save(output_path, quality=95)
            
            # Update progress bar
            pbar.update(1)
            
    except Exception as e:
        print(f"\nError processing {image_path.name}: {str(e)}")
    finally:
        # Force garbage collection
        gc.collect()

def convert_folder_to_nord(input_folder: str, output_folder: str) -> None:
    """Convert all images in a folder to Nord theme versions."""
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Get list of supported image files
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
    image_files = [f for f in input_path.iterdir() 
                  if f.suffix.lower() in supported_formats]
    
    total_images = len(image_files)
    print(f"\nFound {total_images} images to process")
    
    # Calculate optimal number of workers based on CPU cores and memory
    cpu_count = psutil.cpu_count(logical=False)  # Physical cores only
    available_memory_gb = psutil.virtual_memory().available / (1024**3)
    max_workers = min(cpu_count, max(1, int(available_memory_gb / 2)))
    
    print(f"Using {max_workers} worker threads")
    print(f"Available memory: {available_memory_gb:.2f} GB")
    
    start_time = time.time()
    
    # Create progress bar
    with tqdm(total=total_images, desc="Converting images") as pbar:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Process images in parallel
            executor.map(lambda x: process_image(x, output_path, pbar), image_files)
    
    end_time = time.time()
    print(f"\nProcessing complete! Took {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert images to Nord theme color palette')
    parser.add_argument('input_folder', help='Input folder containing wallpapers')
    parser.add_argument('output_folder', help='Output folder for Nord versions')
    
    args = parser.parse_args()
    
    # Required packages notice
    print("Make sure you have the required packages installed:")
    print("pip install Pillow numpy tqdm psutil")
    
    convert_folder_to_nord(args.input_folder, args.output_folder)
