import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)


class FileStat(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        # Поле ввода имени файла
        self.filename_label = QLabel("Имя файла:")
        self.filenameEdit = QLineEdit()
        vbox.addWidget(self.filename_label)
        vbox.addWidget(self.filenameEdit)

        # Кнопка для запуска анализа
        self.button = QPushButton("Анализировать")
        self.button.clicked.connect(self.analyze_file)
        vbox.addWidget(self.button)

        # Поля для вывода результатов
        self.min_label = QLabel("Минимальное значение:")
        self.max_label = QLabel("Максимальное значение:")
        self.avg_label = QLabel("Среднее значение:")

        self.minEdit = QLineEdit()
        self.minEdit.setReadOnly(True)
        self.maxEdit = QLineEdit()
        self.maxEdit.setReadOnly(True)
        self.avgEdit = QLineEdit()
        self.avgEdit.setReadOnly(True)

        vbox.addWidget(self.min_label)
        vbox.addWidget(self.minEdit)
        vbox.addWidget(self.max_label)
        vbox.addWidget(self.maxEdit)
        vbox.addWidget(self.avg_label)
        vbox.addWidget(self.avgEdit)

        self.setLayout(vbox)

    def analyze_file(self):
        # Очистка полей перед анализом
        self.clear_fields()

        # Получение имени файла
        filename = self.filenameEdit.text().strip()

        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            self.show_status_message("Указанный файл не существует")
            return
        except Exception as e:
            self.show_status_message(str(e))
            return

        # Преобразование содержимого файла в список целых чисел
        numbers = []
        for num_str in content.split():
            try:
                num = int(num_str)
                numbers.append(num)
            except ValueError:
                pass

        if not numbers:
            self.show_status_message("Файл содержит некорректные данные")
            return

        # Вычисление минимального, максимального и среднего значения
        minimum = min(numbers)
        maximum = max(numbers)
        average = sum(numbers) / len(numbers)

        # Вывод результатов в поля
        self.minEdit.setText(str(minimum))
        self.maxEdit.setText(str(maximum))
        self.avgEdit.setText(f"{average:.2f}")

        # Сохранение результатов в файл out.txt
        with open('out.txt', 'w') as outfile:
            outfile.write(f'Максимальное значение = {maximum}\n')
            outfile.write(f'Минимальное значение = {minimum}\n')
            outfile.write(f'Среднее значение = {average:.2f}')

    def clear_fields(self):
        """Очищает поля вывода"""
        self.minEdit.clear()
        self.maxEdit.clear()
        self.avgEdit.clear()

    def show_status_message(self, message):
        """Отображает сообщение в статусбаре"""
        main_window.statusBar().showMessage(message)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(FileStat())
        self.setWindowTitle("Анализатор файлов")
        self.setFixedSize(300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())