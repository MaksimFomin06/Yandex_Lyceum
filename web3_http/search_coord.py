import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
)
from PyQt6.QtGui import QPixmap
import requests


class MapViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.server_address = 'https://static-maps.yandex.ru/v1?'
        self.api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'

        # Поля для ввода координат и масштаба
        self.latitude_input = QLineEdit(self)
        self.longitude_input = QLineEdit(self)
        self.scale_input = QLineEdit(self)

        # Кнопка обновления карты
        self.update_button = QPushButton("Обновить карту", self)
        self.update_button.clicked.connect(self.update_map)

        # Метка для отображения карты
        self.map_label = QLabel(self)
        self.map_label.resize(600, 450)

        # Компоновка элементов
        layout = QGridLayout(self)
        layout.addWidget(QLabel("Широта:"), 0, 0)
        layout.addWidget(self.latitude_input, 0, 1)
        layout.addWidget(QLabel("Долгота:"), 1, 0)
        layout.addWidget(self.longitude_input, 1, 1)
        layout.addWidget(QLabel("Масштаб (0.001 - 10):"), 2, 0)
        layout.addWidget(self.scale_input, 2, 1)
        layout.addWidget(self.update_button, 3, 0, 1, 2)
        layout.addWidget(self.map_label, 4, 0, 1, 2)

        # Устанавливаем начальные значения для координат и масштаба
        self.latitude_input.setText("37.530887")
        self.longitude_input.setText("55.703118")
        self.scale_input.setText("0.002")

        # Первоначальное обновление карты
        self.update_map()

        # Настройка основного окна
        self.setWindowTitle('Yandex Maps Viewer')
        self.show()

    def update_map(self):
        latitude = self.latitude_input.text()
        longitude = self.longitude_input.text()
        scale = self.scale_input.text()

        ll_spn = f'll={longitude},{latitude}&spn={scale},{scale}'
        map_request = f"{self.server_address}{ll_spn}&apikey={self.api_key}"

        response = requests.get(map_request)

        if not response.ok:
            print(f"Ошибка выполнения запроса: {response.status_code}")
            return

        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.map_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapViewer()
    sys.exit(app.exec())