from math import cos, radians, sin
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QColor, QPainter, QPen, QPolygonF
from PyQt6.QtWidgets import QApplication, QWidget
import random
import sys

class Suprematism(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Suprematism")
        self.resize(1000, 1000)
        self.show()

        self.shapes = []

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor("black"), 2, Qt.PenStyle.SolidLine)
        painter.setPen(pen)

        for shape in self.shapes:
            color = QColor(*shape['color'])
            painter.setBrush(color)
        if shape['type'] == 'circle':
            radius = shape['size']
            center_x = shape['pos'].x()
            center_y = shape['pos'].y()
            painter.drawEllipse(int(center_x - radius), int(center_y - radius), 2 * radius, 2 * radius)
        elif shape['type'] == 'square':
            size = shape['size']
            top_left_x = int(shape['pos'].x() - size / 2)
            top_left_y = int(shape['pos'].y() - size / 2)
            painter.drawRect(top_left_x, top_left_y, int(size), int(size))
        elif shape['type'] == 'triangle':
            radius = shape['size']
            center_x = shape['pos'].x()
            center_y = shape['pos'].y()
            angle = 360 / 3
            points = [
                QPointF(center_x + radius * cos(radians(angle * i)),
                        center_y + radius * sin(radians(angle * i)))
                for i in range(3)
            ]
            polygon = QPolygonF(points)
            painter.drawPolygon(polygon)
    def mousePressEvent(self, event):
        pos = event.position().toPoint()
        size = random.randint(20, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if event.buttons() & Qt.MouseButton.LeftButton:
            self.shapes.append({'type': 'circle', 'pos': pos, 'size': size, 'color': color})
        elif event.buttons() & Qt.MouseButton.RightButton:
            self.shapes.append({'type': 'square', 'pos': pos, 'size': size, 'color': color})

        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            pos = self.mapFromGlobal(QCursor.pos())
            size = random.randint(20, 100)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.shapes.append({'type': 'triangle', 'pos': pos, 'size': size, 'color': color})
            self.update()

    def clear_shapes(self):
        self.shapes = []
        self.update()

app = QApplication(sys.argv)
window = Suprematism()
sys.exit(app.exec())