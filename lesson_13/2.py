import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6.QtCore import Qt, QEvent


class Car(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 300)
        self.car_images = ['car1.png', 'car2.png', 'car3.png']
        self.current_image_index = 0
        self.lbl = QLabel(self)
        self.pixmap = QPixmap(self.car_images[self.current_image_index])
        self.lbl.setPixmap(self.pixmap)
        self.update_label_position()
        self.setMouseTracking(True)
        self.lbl.installEventFilter(self)

    def update_label_position(self):
        cursor_pos = QCursor.pos()
        local_cursor_pos = self.mapFromGlobal(cursor_pos)

        x = local_cursor_pos.x()
        y = local_cursor_pos.y()

        if x > self.width() - self.lbl.width() // 2:
            x = self.width() - self.lbl.width() // 2
        elif x < self.lbl.width() // 2:
            x = self.lbl.width() // 2
        if y > self.height() - self.lbl.height() // 2:
            y = self.height() - self.lbl.height() // 2
        elif y < self.lbl.height() // 2:
            y = self.lbl.height() // 2

        self.lbl.move(x - self.lbl.width() // 2, y - self.lbl.height() // 2)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.KeyPress:
            key_event = event
            if key_event.key() == Qt.Key.Key_Space:
                self.current_image_index = (self.current_image_index + 1) % len(self.car_images)
                self.pixmap = QPixmap(self.car_images[self.current_image_index])
                self.lbl.setPixmap(self.pixmap)
                return True
        return False

    def mouseMoveEvent(self, event):
        self.update_label_position()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Car()
    ex.show()
    sys.exit(app.exec())