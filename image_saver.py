from PyQt5.QtWidgets import QFileDialog

def save_image(image, app):
    if not image:
        return

    file_dialog = QFileDialog(app)
    save_path, _ = file_dialog.getSaveFileName(app, "save image", "", "png files (*.png);;jpeg files (*.jpg *.jpeg)")

    if save_path:
        image.save(save_path)