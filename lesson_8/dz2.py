import sys
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QPushButton,
)
from PyQt6.QtGui import QPainter, QColor
from random import randint


class RandomFlag(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 400)
        self.base = None
        self.colors = []

        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.label = QLabel("Количество цветов (от 1 до 10):")
        self.spin_box = QSpinBox()
        self.spin_box.setRange(1, 10)
        self.spin_box.setSingleStep(1)
        self.spin_box.setValue(3)
        self.spin_box.valueChanged.connect(self.generate_colors)

        self.button = QPushButton("Создать флаг")
        self.button.clicked.connect(self.paint_flag)

        self.hbox.addWidget(self.label)
        self.hbox.addWidget(self.spin_box)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.setWindowTitle("Random Flag Generator")
        self.show()

    def generate_colors(self):
        num_colors = self.spin_box.value()
        self.colors.clear()
        for _ in range(num_colors):
            self.colors.extend([randint(0, 255), randint(0, 255, exclude_self=0)])
            
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.size().width()
        height = self.size().height()

        if self.base:
            for i in range(len(self.colors)):
                color = QColor(*self.colors[i])
                painter.setPen(color)
                painter.drawRect(0, i * height // len(self.colors), width, height // len(self.colors))

    def paint_flag(self):
        self.base = [(0, 0, self.width, self.height)]
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RandomFlag()
    sys.exit(app.exec())