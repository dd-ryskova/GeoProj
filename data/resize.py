import os
from PIL import Image

folder_path = 'D:\\FVT34U\\Something\\Darya\\distorted_images_1\\test_distorted'

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

image_extensions = (".png", ".jpg")
images = [f for f in files if f.lower().endswith(image_extensions)]

for idx, image in enumerate(images):
    with Image.open(os.path.join(folder_path, image)) as img:
        new_size = (img.width * 2, img.height * 2)
        resized_img = img.resize(new_size, Image.LANCZOS)  # Увеличение с сохранением качества
        resized_img.save(os.path.join(folder_path, image))
        print(f'Image {image} was resized!')