import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class EventManager(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design/design.ui", self)
        self.initUi()

    def initUi(self):
        self.AddButton.clicked.connect(self.add_btn_click)
        self.replaceNameButton.clicked.connect(self.r_name_btn_click)
        self.replaceDateButton.clicked.connect(self.r_date_btn_click)
        self.replaceTimeButton.clicked.connect(self.r_time_btn_click)
        self.replaceGeoButton.clicked.connect(self.r_geo_btn_click)
        self.DeleteButton.clicked.connect(self.d_btn_click)
    
    def add_btn_click(self):
        

    def r_name_btn_click(self):
        

    def r_date_btn_click(self):
        

    def r_time_btn_click(self):
        

    def r_geo_btn_click(self):
        

    def d_btn_click(self):
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EventManager()
    ex.show()
    sys.exit(app.exec())