import os
from PIL import Image

folder_path = 'D:\\FVT34U\\Something\\Darya\\distorted_images_2\\test_distorted'

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

image_extensions = (".png", ".jpg")
images = [f for f in files if f.lower().endswith(image_extensions)]

for idx, image in enumerate(images):
    with open('log.txt', 'a') as file:
        file.write(f'{image}, {Image.open(os.path.join(folder_path, image)).size}\n')