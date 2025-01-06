import sys
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSlider,
)
from PyQt6.QtGui import QPixmap, qRgba
from PyQt6.QtCore import Qt


class AlphaManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 400)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap("orig.jpg")
        self.alpha = QSlider(Qt.Orientation.Horizontal)
        self.alpha.setRange(0, 255)
        self.alpha.valueChanged.connect(self.on_alpha_changed)
        self.alpha_label = QLabel(f"Текущая прозрачность: {self.alpha.value()}")
        self.image_label = QLabel()
        self.image_label.setPixmap(self.pixmap)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.alpha_label)
        hbox.addWidget(self.alpha)
        vbox.addLayout(hbox)
        vbox.addWidget(self.image_label)
        self.setLayout(vbox)
        self.setWindowTitle("Управление прозрачностью")
        self.show()

    def on_alpha_changed(self, value):
        self.alpha_label.setText(f"Текущая прозрачность: {value}")
        image = self.apply_transparency(value)
        image.save("new.png", "png")
        self.image_label.setPixmap(QPixmap.fromImage(image))

    def apply_transparency(self, alpha_value):
        image = self.pixmap.toImage()
        for x in range(image.width()):
            for y in range(image.height()):
                pixel_color = image.pixelColor(x, y)
                new_pixel_color = qRgba(pixel_color.red(), pixel_color.green(), pixel_color.blue(), alpha_value)
                image.setPixelColor(x, y, new_pixel_color)
        return image


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    sys.exit(app.exec())