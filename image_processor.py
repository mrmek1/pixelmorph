from PIL import Image
import numpy as np
from PyQt5.QtGui import QImage

def process_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert("RGB")
        pixels = np.array(image)

        sorted_pixels = sort_pixels_vertically(pixels)

        sorted_image = Image.fromarray(sorted_pixels)

        q_image = QImage(sorted_image.tobytes(), sorted_image.width, sorted_image.height, sorted_image.width * 3, QImage.Format_RGB888)

        return q_image

    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def sort_pixels_vertically(pixels):
    height, width, _ = pixels.shape

    for x in range(width):
        column_pixels = pixels[:, x, :]
        column_brightness = np.sum(column_pixels, axis=1)
        sorted_column = column_pixels[np.argsort(column_brightness)]
        pixels[:, x, :] = sorted_column

    return pixels