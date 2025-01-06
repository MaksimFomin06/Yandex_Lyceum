import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QCheckBox, QPushButton, QPlainTextEdit,
                             QLabel)


class MacOrder(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Заказ в Макдональдсе")

        # Создаем вертикальный компоновщик
        self.layout = QVBoxLayout()

        # Определяем меню и создаём чекбоксы
        self.menu_items = ["Чизбургер", "Гамбургер", "Кока-кола", "Наггетсы"]
        self.menu_checkboxes = []

        for item in self.menu_items:
            checkbox = QCheckBox(item)
            self.menu_checkboxes.append(checkbox)
            self.layout.addWidget(checkbox)

        # Кнопка Заказать
        self.order_btn = QPushButton("Заказать")
        self.order_btn.clicked.connect(self.place_order)  # Подключаем событие нажатия кнопки
        self.layout.addWidget(self.order_btn)

        # Область для отображения результата
        self.result = QPlainTextEdit()
        self.result.setReadOnly(True)
        self.layout.addWidget(QLabel("Ваш заказ: (чек)"))
        self.layout.addWidget(self.result)

        # Устанавливаем компоновщик в виджет
        self.setLayout(self.layout)

    def place_order(self):
        # Собираем заказ
        order_items = []
        for checkbox in self.menu_checkboxes:
            if checkbox.isChecked():
                order_items.append(checkbox.text())

        # Формируем текст заказа
        if order_items:
            order_text = "Ваш заказ:\n\n" + "\n".join(order_items)
        else:
            order_text = "Ваш заказ пуст."

        # Отображаем результат в текстовом поле
        self.result.setPlainText(order_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MacOrder()
    window.resize(300, 400)
    window.show()
    sys.exit(app.exec())