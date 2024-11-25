import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.init_ui()

    def init_ui(self):
        self.pushButton.clicked.connect(self.draw_circle)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("yellow"), 2)
        painter.setPen(pen)

        if hasattr(self, 'circle'):
            painter.drawEllipse(*self.circle)

    def draw_circle(self):
        width = self.width()
        height = self.height()

        x = randint(0, width)
        y = randint(0, height)
        diameter = randint(10, min(width, height))

        self.circle = (x, y, diameter, diameter)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())