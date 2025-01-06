import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QWidget,
)
from PyQt6.QtCore import Qt


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(250, 350)

        # Основной контейнер
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основная разметка
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Верхний лейбл для отображения результата
        self.result_label = QLabel(alignment=Qt.AlignmentFlag.AlignRight)
        self.result_label.setText("0")
        layout.addWidget(self.result_label)

        # Нижний лейбл для отображения промежуточных результатов
        self.history_label = QLabel(alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.history_label)

        # Разметка для кнопок
        buttons_layout = QGridLayout()
        layout.addLayout(buttons_layout)

        # Список кнопок
        self.buttons = {}

        # Цифровые кнопки
        for i in range(1, 10):
            row = ((i - 1) // 3) + 2
            col = (i - 1) % 3
            btn = QPushButton(str(i))
            self.buttons[str(i)] = btn
            buttons_layout.addWidget(btn, row, col)

        # Кнопка 0
        self.buttons["0"] = QPushButton("0")
        buttons_layout.addWidget(self.buttons["0"], 5, 0, 1, 2)

        # Кнопка точки
        self.buttons["."] = QPushButton(".")
        buttons_layout.addWidget(self.buttons["."], 5, 2)

        # Кнопка смены знака
        self.buttons["±"] = QPushButton("±")
        buttons_layout.addWidget(self.buttons["±"], 1, 0)

        # Кнопка очистки ввода
        self.buttons["CE"] = QPushButton("CE")
        buttons_layout.addWidget(self.buttons["CE"], 1, 1)

        # Кнопка полной очистки
        self.buttons["C"] = QPushButton("C")
        buttons_layout.addWidget(self.buttons["C"], 1, 2)

        # Кнопки операторов
        self.add_button = ["/", "*", "-", "+"]
        for i, op in enumerate(self.add_button):
            self.buttons[op] = QPushButton(op)
            buttons_layout.addWidget(self.buttons[op], i + 2, 3)

        # Кнопка равенства
        self.buttons["="] = QPushButton("=")
        buttons_layout.addWidget(self.buttons["="], 5, 3)

        # Подключение сигналов кнопок
        self.connect_buttons()

    def connect_buttons(self):
        for key, btn in self.buttons.items():
            if key.isdigit() or key == ".":
                btn.clicked.connect(lambda _, k=key: self.on_digit_clicked(k))
            elif key == "=":
                btn.clicked.connect(self.on_equals_clicked)
            elif key == "C":
                btn.clicked.connect(self.on_clear_clicked)
            elif key == "CE":
                btn.clicked.connect(self.on_clear_entry_clicked)
            elif key == "±":
                btn.clicked.connect(self.on_plus_minus_clicked)
            else:
                btn.clicked.connect(lambda _, k=key: self.on_operator_clicked(k))

    def on_digit_clicked(self, digit):
        current_text = self.result_label.text()
        if current_text == "0" or self.error_state:
            self.result_label.setText(digit)
        else:
            new_text = current_text + digit
            if len(new_text) <= 11:
                self.result_label.setText(new_text)

    def on_operator_clicked(self, operator):
        current_text = self.result_label.text()
        history_text = self.history_label.text()

        if current_text != "" and not self.error_state:
            if history_text == "":
                self.history_label.setText(f"{current_text} {operator}")
            else:
                self.history_label.setText(f"{history_text} {current_text} {operator}")
            self.result_label.setText("")

    def on_equals_clicked(self):
        current_text = self.result_label.text()
        history_text = self.history_label.text()

        if current_text != "" and not self.error_state:
            try:
                expression = history_text + " " + current_text
                result = eval(expression)
                self.result_label.setText(str(result))
                self.history_label.setText("")
            except ZeroDivisionError:
                self.result_label.setText("ОШИБКА")
                self.history_label.setText("")
                self.error_state = True

    def on_clear_clicked(self):
        self.result_label.setText("0")
        self.history_label.setText("")
        self.error_state = False

    def on_clear_entry_clicked(self):
        self.result_label.setText("0")

    def on_plus_minus_clicked(self):
        current_text = self.result_label.text()
        if current_text != "0" and not self.error_state:
            self.result_label.setText(str(-float(current_text)))

    @property
    def error_state(self):
        return self.result_label.text() == "ОШИБКА"

    @error_state.setter
    def error_state(self, value):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())