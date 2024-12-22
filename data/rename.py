import os

folder_path = 'D:\\FVT34U\\Something\\Darya\\archive\\v_2\\grassland\\s2'

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

image_extensions = (".png", ".jpg")
images = [f for f in files if f.lower().endswith(image_extensions)]

for idx, image in enumerate(images):
    new_name = f"{idx:06}.jpg"  # Формат 000001.jpg
    old_path = os.path.join(folder_path, image)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)