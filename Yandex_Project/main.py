import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class EventManager(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design/design.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EventManager()
    ex.show()
    sys.exit(app.exec())