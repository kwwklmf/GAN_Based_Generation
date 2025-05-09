import os
import random
import shutil

# Function to randomly select images

def random_select_images(source_folder, destination_folder, num_images):
    # Get list of all files in the source folder
    all_files = os.listdir(source_folder)
    
    # Filter out non-image files (assuming images have common extensions)
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
    
    # Check if the number of images requested is more than available
    if num_images > len(image_files):
        raise ValueError("Number of images requested exceeds the number of available images.")
    
    # Randomly select the specified number of images
    selected_images = random.sample(image_files, num_images)
    
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    # Move selected images to the destination folder and delete from source
    for image in selected_images:
        shutil.move(os.path.join(source_folder, image), os.path.join(destination_folder, image))
        # Delete the image from the source folder

# Example usage
source_folder = '/home/kongweiwen/github_code/pytorch-CycleGAN-and-pix2pix/datasets/cars_BtoA/train'
destination_folder = '/home/kongweiwen/github_code/pytorch-CycleGAN-and-pix2pix/datasets/cars_BtoA/val'
num_images = 900
random_select_images(source_folder, destination_folder, num_images)
