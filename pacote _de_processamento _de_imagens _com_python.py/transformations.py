from PIL import Image

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    return image.resize((width, height))