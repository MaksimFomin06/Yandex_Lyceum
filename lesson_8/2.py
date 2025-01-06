import sys
from math import floor
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QGridLayout,
)
from PyQt6.QtGui import QPainter, QPen, QColor, QRectF
from PyQt6.QtCore import Qt


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Квадрат-объектив — 1")
        self.resize(800, 900)
        self.color = QColor(Qt.GlobalColor.red)
        self.create_controls()
        self.layout_widgets()
        self.lineEdit.setText('300')
        self.lineEdit_2.setText('0.9')
        self.lineEdit_3.setText('10')

    def create_controls(self):
        self.label_a = QLabel("Размер стороны квадрата:")
        self.lineEdit = QLineEdit()
        self.label_k = QLabel("Коэффициент масштабирования:")
        self.lineEdit_2 = QLineEdit()
        self.label_n = QLabel("Количество квадратов:")
        self.lineEdit_3 = QLineEdit()
        self.btn = QPushButton("Построить квадраты")
        self.btn.clicked.connect(self.draw_squares)

    def layout_widgets(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.label_a, 0, 0)
        grid_layout.addWidget(self.lineEdit, 0, 1)
        grid_layout.addWidget(self.label_k, 1, 0)
        grid_layout.addWidget(self.lineEdit_2, 1, 1)
        grid_layout.addWidget(self.label_n, 2, 0)
        grid_layout.addWidget(self.lineEdit_3, 2, 1)
        main_layout.addLayout(grid_layout)
        main_layout.addStretch()
        main_layout.addWidget(self.btn)
        self.setLayout(main_layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen(self.color, 2, Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        x_center = 400
        y_center = 450
        try:
            a = float(self.lineEdit.text())
            k = float(self.lineEdit_2.text())
            n = int(self.lineEdit_3.text())
        except ValueError:
            return
        if not (a > 0 and 0 < k < 1 and n >= 1):
            return
        for i in range(n):
            size = a * pow(k, i)
            rect = QRectF(x_center - size / 2, y_center - size / 2, size, size)
            painter.drawRect(rect)

    def draw_squares(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Square1()
    window.show()
    sys.exit(app.exec())