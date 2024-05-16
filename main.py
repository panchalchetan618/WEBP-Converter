import os
from PIL import Image, UnidentifiedImageError

def convert_images_to_webp(folder_path):
    image_formats = ('.png', '.jpg', '.jpeg')

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_formats):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    # Get the base filename without extension
                    base_filename = os.path.splitext(filename)[0]
                    webp_path = os.path.join(folder_path, base_filename + '.webp')
                    img.save(webp_path, 'webp')
                    print(f'Converted {file_path} to {webp_path}')
            except UnidentifiedImageError:
                print(f'Cannot identify image file {file_path}')
            except Exception as e:
                print(f'Error processing {file_path}: {e}')

folder_path = input("Enter folder path where image(s) are stored: ")
convert_images_to_webp(folder_path)
