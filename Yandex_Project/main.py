import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDateEdit, QTimeEdit
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class EventManager(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design/design.ui", self)
        self.initUi()

    def initUi(self):
        self.label_error.hide()

        self.AddButton.clicked.connect(self.add_btn_click)
        self.replaceNameButton.clicked.connect(self.r_name_btn_click)
        self.replaceDateButton.clicked.connect(self.r_date_btn_click)
        self.replaceTimeButton.clicked.connect(self.r_time_btn_click)
        self.replaceGeoButton.clicked.connect(self.r_geo_btn_click)
        self.DeleteButton.clicked.connect(self.d_btn_click)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data/EventManager_db.sqlite")

    def add_btn_click(self):
        self.db.open()
        input_name = self.input_name.text()
        input_date = self.input_date.date()
        input_date = input_date.toString("dd.MM.yyyy")
        input_time = self.input_time.time()
        input_time = input_time.toString("hh:mm")
        input_geo = self.input_geo.text()
        
        if not all([input_name, input_date, input_time, input_geo]):
            self.label_error.show()
        else:
            self.label_error.hide()
            request = QSqlQuery(self.db)
            query = f"INSERT INTO events VALUES('{input_name}', '{input_date}', '{input_time}', '{input_geo}')"
            request.exec(query)
        self.db.close()


    def r_name_btn_click(self):
        pass

    def r_date_btn_click(self):
        pass

    def r_time_btn_click(self):
        pass

    def r_geo_btn_click(self):
        pass

    def d_btn_click(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EventManager()
    ex.show()
    sys.exit(app.exec())