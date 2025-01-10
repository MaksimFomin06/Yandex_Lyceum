import sys
from random import randint
from math import cos, sin
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QBrush, QCursor, QPolygon
from PyQt6.QtCore import Qt, QPoint


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1000, 1000)
        self.setMouseTracking(True)
        self.show()
        self.shapes = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for shape in self.shapes:
            if shape['type'] == 'circle':
                radius = shape['radius']
                center = shape['center']
                color = shape['color']
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QBrush(color))
                painter.drawEllipse(center, radius, radius)
            elif shape['type'] == 'square':
                size = shape['size']
                top_left = shape['top_left']
                color = shape['color']
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QBrush(color))
                painter.drawRect(top_left.x(), top_left.y(), size, size)
            elif shape['type'] == 'triangle':
                points = shape['points']
                color = shape['color']
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QBrush(color))
                polygon = QPolygon(points)
                painter.drawPolygon(polygon)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.add_circle(event.pos())
        elif event.button() == Qt.MouseButton.RightButton:
            self.add_square(event.pos())
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.add_triangle(self.mapFromGlobal(QCursor.pos()))
            self.update()

    def add_circle(self, pos):
        radius = randint(20, 100)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.shapes.append({
            'type': 'circle',
            'radius': radius,
            'center': pos,
            'color': color
        })

    def add_square(self, pos):
        size = randint(20, 100)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        top_left = QPoint(pos.x() - size / 2, pos.y() - size / 2)
        self.shapes.append({
            'type': 'square',
            'size': size,
            'top_left': top_left,
            'color': color
        })

    def add_triangle(self, pos):
        radius = randint(20, 100)
        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        angle = 2 * 3.141592653589793 / 3
        points = [
            QPoint(pos.x(), pos.y()),
            QPoint(pos.x() + radius * cos(angle), pos.y() + radius * sin(angle)),
            QPoint(pos.x() + radius * cos(2 * angle), pos.y() + radius * sin(2 * angle))
        ]
        self.shapes.append({
            'type': 'triangle',
            'points': points,
            'color': color
        })


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Suprematism()
    sys.exit(app.exec())