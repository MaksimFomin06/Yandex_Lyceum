import sys
import csv
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QComboBox
)


class OlympResult(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Olympiad Results Filter')

        layout = QVBoxLayout()
        filter_layout = QHBoxLayout()

        label_school = QLabel('Школа:')
        self.schools = QComboBox()
        self.schools.addItem('-- Все школы --')
        self.populate_schools()

        label_class = QLabel('Класс:')
        self.classes = QComboBox()
        self.classes.addItem('-- Все классы --')
        self.populate_classes()

        self.result_button = QPushButton('Фильтровать')
        self.result_button.clicked.connect(self.filter_results)

        filter_layout.addWidget(label_school)
        filter_layout.addWidget(self.schools)
        filter_layout.addWidget(label_class)
        filter_layout.addWidget(self.classes)
        filter_layout.addWidget(self.result_button)

        self.table_widget = QTableWidget()
        self.load_data()

        layout.addLayout(filter_layout)
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

    def populate_schools(self):
        """Заполняет выпадающий список школ значениями из файла."""
        schools_set = set()
        with open('rez.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                login = row['login']
                school_number = login.split('-')[2]
                schools_set.add(school_number)

        for school in sorted(list(schools_set)):
            self.schools.addItem(school)

    def populate_classes(self):
        """Заполняет выпадающий список классов значениями из файла."""
        classes_set = set()
        with open('rez.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                login = row['login']
                class_number = login.split('-')[3]
                classes_set.add(class_number)

        for _class in sorted(list(classes_set)):
            self.classes.addItem(_class)

    def load_data(self):
        """Загружает данные из CSV-файла и заполняет таблицу."""
        headers = ['Место', 'Имя участника', 'Логин', '1(Система счисления)', '2(Количество символов)',
                   '3(Минимальное число)', '4(Трамвай)', 'Сумма баллов']
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setHorizontalHeaderLabels(headers)

        with open('rez.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.table_widget.setRowCount(len(rows))

            for i, row in enumerate(rows):
                items = [
                    QTableWidgetItem(str(i+1)),
                    QTableWidgetItem(row['user_name']),
                    QTableWidgetItem(row['login']),
                    QTableWidgetItem(row['1(Система счисления)']),
                    QTableWidgetItem(row['2(Количество символов)']),
                    QTableWidgetItem(row['3(Минимальное число)']),
                    QTableWidgetItem(row['4(Трамвай)']),
                    QTableWidgetItem(row['Score'])
                ]
                for j, item in enumerate(items):
                    self.table_widget.setItem(i, j, item)

    def filter_results(self):
        """Применяет фильтры и обновляет таблицу."""
        selected_school = self.schools.currentText()
        selected_class = self.classes.currentText()

        filtered_rows = []
        with open('rez.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                login = row['login']
                school_number = login.split('-')[2]
                class_number = login.split('-')[3]

                if (selected_school == '-- Все школы --' or selected_school == school_number) \
                        and (selected_class == '-- Все классы --' or selected_class == class_number):
                    filtered_rows.append(row)

        self.table_widget.clearContents()
        self.table_widget.setRowCount(len(filtered_rows))

        for i, row in enumerate(filtered_rows):
            items = [
                QTableWidgetItem(str(i+1)),
                QTableWidgetItem(row['user_name']),
                QTableWidgetItem(row['login']),
                QTableWidgetItem(row['1(Система счисления)']),
                QTableWidgetItem(row['2(Количество символов)']),
                QTableWidgetItem(row['3(Минимальное число)']),
                QTableWidgetItem(row['4(Трамвай)']),
                QTableWidgetItem(row['Score'])
            ]
            for j, item in enumerate(items):
                self.table_widget.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OlympResult()
    ex.show()
    sys.exit(app.exec())