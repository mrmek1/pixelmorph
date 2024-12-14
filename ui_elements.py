from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QGraphicsOpacityEffect
from animations import fade_in_animation, fade_out_animation, button_click_animation, slide_in_animation
from image_loader import load_image
from image_processor import process_image
from image_saver import save_image as save_image_func

class PixelMorphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PixelMorph - Image Pixel Sorter")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;") 

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.title_label = QLabel("PixelMorph", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.title_label.setStyleSheet("color: #333333;")  
        self.layout.addWidget(self.title_label)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.load_button = QPushButton("Load Image", self)
        self.load_button.clicked.connect(self.load_image)
        self.load_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            transition: background-color 0.3s ease, transform 0.3s ease;
        """)
        self.load_button.setStyleSheet(self.add_hover_effect("#4CAF50", "#45a049"))
        self.layout.addWidget(self.load_button)

        self.sort_button = QPushButton("Sort Pixels", self)
        self.sort_button.clicked.connect(self.sort_pixels)
        self.sort_button.setDisabled(True)
        self.sort_button.setStyleSheet("""
            background-color: #2196F3;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            transition: background-color 0.3s ease, transform 0.3s ease;
        """)
        self.sort_button.setStyleSheet(self.add_hover_effect("#2196F3", "#1976D2"))
        self.layout.addWidget(self.sort_button)

        self.save_button = QPushButton("Save Image", self)
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setDisabled(True)
        self.save_button.setStyleSheet("""
            background-color: #FF9800;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
            transition: background-color 0.3s ease, transform 0.3s ease;
        """)
        self.save_button.setStyleSheet(self.add_hover_effect("#FF9800", "#FB8C00"))
        self.layout.addWidget(self.save_button)

        self.opacity_effect = QGraphicsOpacityEffect()
        self.image_label.setGraphicsEffect(self.opacity_effect)

        self.image_path = None
        self.image = None

    def load_image(self):
        """load image"""
        self.image_path, self.image = load_image(self)
        if self.image:
            self.image_label.setPixmap(self.image.scaled(800, 500, Qt.KeepAspectRatio))
            self.sort_button.setEnabled(True)
            self.fade_in_animation()

    def fade_in_animation(self):
        """fade in animation"""
        self.fade_in = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_in.setDuration(1000)  
        self.fade_in.setStartValue(0)
        self.fade_in.setEndValue(1)
        self.fade_in.start()

    def sort_pixels(self):
        """sort pixels"""
        if not self.image_path:
            return
        
        processed_image = process_image(self.image_path)

        if processed_image:
            self.image = QPixmap.fromImage(processed_image)
            self.image_label.setPixmap(self.image.scaled(800, 500, Qt.KeepAspectRatio))
            self.save_button.setEnabled(True)

    def save_image(self):
        """save image"""
        save_image_func(self.image, self)  

    def add_hover_effect(self, base_color, hover_color):
        """add hover effect"""
        return f"""
            QPushButton {{
                background-color: {base_color};
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
                transition: background-color 0.3s ease, transform 0.3s ease;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
                transform: scale(1.1);
            }}
            QPushButton:disabled {{
                background-color: #D3D3D3;
                color: #A9A9A9;
                transform: none;
            }}
        """