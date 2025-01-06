import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QGroupBox,
    QRadioButton,
    QFileDialog,
    QLabel,
)
from PyQt6.QtGui import QImage, QPixmap, QTransform, QColor


class MyPillow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 400)
        self.curr_image = None
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        # Добавляем кнопку для загрузки изображения
        load_button = QPushButton("Загрузить изображение")
        load_button.clicked.connect(self.load_image)
        layout.addWidget(load_button, 0, 0)

        # Группа для управления каналами
        self.channel_group = QGroupBox("Цветовые каналы")
        self.red_channel = QRadioButton("Красный канал")
        self.green_channel = QRadioButton("Зелёный канал")
        self.blue_channel = QRadioButton("Синий канал")
        self.all_channels = QRadioButton("Все каналы")
        self.all_channels.setChecked(True)

        self.channelButtons = QGroupBox("Управление цветами")
        self.channelButtons.setCheckable(False)
        self.channelButtons.setChecked(False)

        self.channel_layout = QGridLayout(self.channelButtons)
        self.channel_layout.addWidget(self.red_channel, 0, 0)
        self.channel_layout.addWidget(self.green_channel, 0, 1)
        self.channel_layout.addWidget(self.blue_channel, 1, 0)
        self.channel_layout.addWidget(self.all_channels, 1, 1)

        self.channel_group.setLayout(self.channel_layout)
        layout.addWidget(self.channel_group, 1, 0)

        # Группа для поворота изображения
        self.rotate_group = QGroupBox("Поворот изображения")
        self.rotate_left = QPushButton("Повернуть влево")
        self.rotate_right = QPushButton("Повернуть вправо")

        self.rotate_buttons = QGroupBox("Поворот")
        self.rotate_buttons.setCheckable(False)
        self.rotate_buttons.setChecked(False)

        self.rotate_layout = QGridLayout(self.rotate_buttons)
        self.rotate_layout.addWidget(self.rotate_left, 0, 0)
        self.rotate_layout.addWidget(self.rotate_right, 0, 1)

        self.rotate_group.setLayout(self.rotate_layout)
        layout.addWidget(self.rotate_group, 1, 1)

        # Виджет для отображения изображения
        self.image_label = QLabel("")
        layout.addWidget(self.image_label, 0, 1, 2, 1)

        # Подключение сигналов
        self.red_channel.toggled.connect(lambda checked: self.update_image())
        self.green_channel.toggled.connect(lambda checked: self.update_image())
        self.blue_channel.toggled.connect(lambda checked: self.update_image())
        self.all_channels.toggled.connect(lambda checked: self.update_image())

        self.rotate_left.clicked.connect(self.rotate_left_action)
        self.rotate_right.clicked.connect(self.rotate_right_action)

        self.setWindowTitle("MyPillow")
        self.show()

    def update_image(self):
        if self.curr_image is None:
            return

        image = self.curr_image.copy()

        if self.red_channel.isChecked():
            for x in range(image.width()):
                for y in range(image.height()):
                    pixel_color = image.pixelColor(x, y)
                    image.setPixelColor(x, y, QColor(pixel_color.red(), 0, 0))

        elif self.green_channel.isChecked():
            for x in range(image.width()):
                for y in range(image.height()):
                    pixel_color = image.pixelColor(x, y)
                    image.setPixelColor(x, y, QColor(0, pixel_color.green(), 0))

        elif self.blue_channel.isChecked():
            for x in range(image.width()):
                for y in range(image.height()):
                    pixel_color = image.pixelColor(x, y)
                    image.setPixelColor(x, y, QColor(0, 0, pixel_color.blue()))

        elif self.all_channels.isChecked():
            image = self.curr_image

        pixmap = QPixmap.fromImage(image)
        self.image_label.setPixmap(pixmap)

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(None, "Выберите изображение", "", "Images (*.png *.jpg)")

        if file_name:
            self.curr_image = QImage(file_name)
            self.image_label.setPixmap(QPixmap.fromImage(self.curr_image))
            self.channelButtons.setChecked(True)
            self.rotate_buttons.setChecked(True)

    def rotate_left_action(self):
        transform = QTransform()
        transform.rotate(-90)
        transformed_image = self.curr_image.transformed(transform)
        self.curr_image = transformed_image.mirrored(False, True)
        self.update_image()

    def rotate_right_action(self):
        transform = QTransform()
        transform.rotate(90)
        transformed_image = self.curr_image.transformed(transform)
        self.curr_image = transformed_image.mirrored(True, False)
        self.update_image()


if __name__ == "__main__":
    app = QApplication([])
    window = MyPillow()
    sys.exit(app.exec())