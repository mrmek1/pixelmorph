from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

def load_image(app):
    file_dialog = QFileDialog(app)
    file_path, _ = file_dialog.getOpenFileName(app, "select image", "", "image files (*.png *.jpg *.jpeg)")

    if file_path:
        image = QPixmap(file_path)
        return file_path, image
    return None, None