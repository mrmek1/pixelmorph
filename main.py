from PyQt5.QtWidgets import QApplication
import sys
from ui_elements import PixelMorphApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PixelMorphApp()
    window.show()
    sys.exit(app.exec_())