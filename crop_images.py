# script that resizes images to size whilst keeping aspect ratio
# usage: python crop_images.py <size> <input_folder> <output_folder>
import os
import sys
from PIL import Image

def fit_image(input_image_path, output_image_path, target_width, target_height):
    with Image.open(input_image_path) as img:
        img_width, img_height = img.size
        # Calculate the scale factor while maintaining the aspect ratio
        scale = min(target_width / img_width, target_height / img_height)

        # Calculate the new image size
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)

        # Resize the image
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Create a new image with a black background
        new_img = Image.new('RGB', (target_width, target_height), (0, 0, 0))

        # Calculate the position to paste the resized image
        x = (target_width - new_width) // 2
        y = (target_height - new_height) // 2
        new_img.paste(img, (x, y))

        # Save the new image
        new_img.save(output_image_path)

def crop_images(width, height, input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_image_path = os.path.join(input_folder, file_name)
            output_image_path = os.path.join(output_folder, file_name)
            fit_image(input_image_path, output_image_path, width, height)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py width height input_folder output_folder")
        sys.exit(1)

    width, height = int(sys.argv[1]), int(sys.argv[2])
    input_folder, output_folder = sys.argv[3], sys.argv[4]
    crop_images(width, height, input_folder, output_folder)
