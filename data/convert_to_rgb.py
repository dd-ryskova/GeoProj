from PIL import Image

path = "D:\\FVT34U\\Something\\Darya\\testing_data\\exp6\\imgs\\000000.jpg"

img = Image.open(path).convert('L')

img_rgb = img.convert('RGB')

img_rgb.save(path)
