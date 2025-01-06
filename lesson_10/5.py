from pathlib import Path
import os
import sys
import csv
import random
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt


class Expensive(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.tableWidget = QTableWidget()
        self.load_data_from_csv(Path(os.getcwd()) / 'price.csv')
        layout.addWidget(self.tableWidget)

        self.updateButton = QPushButton("Обновить цвета")
        self.updateButton.clicked.connect(self.update_colors)
        layout.addWidget(self.updateButton)

        self.resize_table_columns_to_contents()
        self.highlight_top_five_prices()

    def load_data_from_csv(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            header = next(reader)
            self.tableWidget.setColumnCount(len(header))
            self.tableWidget.setHorizontalHeaderLabels(header)
            self.tableWidget.setRowCount(0)

            rows = []
            for row_number, row in enumerate(reader):
                rows.append([float(row[1]) if i == 1 else row[i] for i in range(len(row))])

            rows.sort(key=lambda x: x[1], reverse=True)

            for row_number, row in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row):
                    item = QTableWidgetItem(str(data))
                    self.tableWidget.setItem(row_number, column_number, item)

    def resize_table_columns_to_contents(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def highlight_top_five_prices(self):
        for row in range(5):
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for col in range(self.tableWidget.columnCount()):
                self.tableWidget.item(row, col).setBackground(color)

    def update_colors(self):
        self.clear_highlight()
        self.highlight_top_five_prices()

    def clear_highlight(self):
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                self.tableWidget.item(row, col).setBackground(Qt.GlobalColor.white)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Expensive()
    window.show()
    sys.exit(app.exec())