from pathlib import Path
import os
import sys
import csv

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
)
from PyQt6.QtCore import Qt


class InteractiveReceipt(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.tableWidget = QTableWidget()
        self.load_data_from_csv(Path(os.getcwd()) / 'price.csv')
        layout.addWidget(self.tableWidget)

        hbox_layout = QHBoxLayout()
        label = QLabel("Итого:")
        self.total = QLineEdit()
        self.total.setReadOnly(True)
        self.update_total_sum()
        hbox_layout.addWidget(label)
        hbox_layout.addWidget(self.total)
        layout.addLayout(hbox_layout)

        self.tableWidget.cellChanged.connect(self.on_cell_changed)

    def load_data_from_csv(self, filepath):
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            header = next(reader)
            self.tableWidget.setColumnCount(len(header) + 1)
            self.tableWidget.setHorizontalHeaderLabels(['Название', 'Цена', 'Количество'])
            self.tableWidget.setRowCount(0)

            for row_number, row in enumerate(reader):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row):
                    item = QTableWidgetItem(data)
                    self.tableWidget.setItem(row_number, column_number, item)

                quantity_item = QTableWidgetItem('0')
                self.tableWidget.setItem(row_number, 2, quantity_item)

    def on_cell_changed(self, row, column):
        if column == 2:
            self.update_total_sum()

    def update_total_sum(self):
        total_sum = 0
        for row in range(self.tableWidget.rowCount()):
            try:
                price = float(self.tableWidget.item(row, 1).text())
                quantity = int(self.tableWidget.item(row, 2).text())
                total_sum += price * quantity
            except ValueError:
                pass
        self.total.setText(str(total_sum))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InteractiveReceipt()
    window.show()
    sys.exit(app.exec())