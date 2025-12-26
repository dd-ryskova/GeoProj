import os

folder_path = 'D:\\FVT34U\\Something\\Darya\\distorted_images_7\\test_flow'

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

image_extensions = (".mat")
images = [f for f in files if f.lower().endswith(image_extensions)]

for idx, image in enumerate(images):
    new_name = f"distorted_{3000 + idx:06}.mat"  # Формат 000001.jpg
    old_path = os.path.join(folder_path, image)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)