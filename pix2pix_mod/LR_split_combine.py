import os
import random
from PIL import Image

# Function to process images

def process_images(source_folder, num_images):
    # Get list of all files in the source folder
    all_files = os.listdir(source_folder)
    
    # Filter out non-image files (assuming images have common extensions)
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
    
    # Check if the number of images requested is more than available
    if num_images > len(image_files):
        raise ValueError("Number of images requested exceeds the number of available images.")
    
    # Randomly select the specified number of images
    selected_images = random.sample(image_files, num_images)
    
    # Process each selected image
    for image_name in selected_images:
        image_path = os.path.join(source_folder, image_name)
        with Image.open(image_path) as img:
            width, height = img.size
            
            # Split the image into left and right halves
            left_half = img.crop((0, 0, width // 2, height))
            right_half = img.crop((width // 2, 0, width, height))
            
            # Mirror each half
            left_half = left_half.transpose(Image.FLIP_LEFT_RIGHT)
            right_half = right_half.transpose(Image.FLIP_LEFT_RIGHT)
            
            # Combine the mirrored halves
            new_img = Image.new('RGB', (width, height))
            new_img.paste(left_half, (0, 0))
            new_img.paste(right_half, (width // 2, 0))
            
            # Save the new image, overwriting the original
            new_img.save(image_path)

# Example usage
source_folder = '/home/kongweiwen/github_code/pytorch-CycleGAN-and-pix2pix/datasets/cars_BtoA/train'
num_images = 1000
process_images(source_folder, num_images)
