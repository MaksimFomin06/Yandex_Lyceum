import sys
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QSlider,
)
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class GoodMoodRising(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1000, 1000)
        self.color = QColor(Qt.GlobalColor.yellow)

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.move(970, 40)
        self.slider.setFixedWidth(20)
        self.slider.setFixedHeight(500)
        self.slider.valueChanged.connect(self.update)

        self.setWindowTitle("Good Mood Rising")
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(self.color)

        size = self.slider.value()

        painter.drawEllipse(0, 0, 10 * size, 10 * size)

        painter.drawEllipse(2 * size, 2 * size, 2 * size, 2 * size)

        painter.drawEllipse(6 * size, 2 * size, 2 * size, 2 * size)

        painter.drawArc(2 * size, 6 * size, 6 * size, 2 * size, -480, -1920)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    sys.exit(app.exec())