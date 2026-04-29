import os
import shutil

# Set your root folder path
root_folder = "path/to/your/root/folder"

# Create a folder to store all images
output_folder = os.path.join(root_folder, "all_images")
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
image_extensions = (".png", ".jpg", ".jpeg", ".JPG", ".JPEG", ".PNG")

# Walk through all subfolders
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith(image_extensions):
            source_path = os.path.join(foldername, filename)
            
            # Handle duplicate names
            new_filename = filename
            counter = 1
            while os.path.exists(os.path.join(output_folder, new_filename)):
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{counter}{ext}"
                counter += 1

            destination_path = os.path.join(output_folder, new_filename)

            # Copy (use shutil.move if you want to MOVE instead)
            shutil.copy2(source_path, destination_path)

print("All images collected successfully!")
