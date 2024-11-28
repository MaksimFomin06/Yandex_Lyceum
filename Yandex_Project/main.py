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
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data/EventManager_db.sqlite")

        self.fill_lst()
        self.label_error.hide()

        self.AddButton.clicked.connect(self.add_btn_click)
        self.replaceNameButton.clicked.connect(self.r_name_btn_click)
        self.replaceDateButton.clicked.connect(self.r_date_btn_click)
        self.replaceTimeButton.clicked.connect(self.r_time_btn_click)
        self.replaceGeoButton.clicked.connect(self.r_geo_btn_click)
        self.DeleteButton.clicked.connect(self.d_btn_click)

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
        input_name = self.input_replace_box.currentText()
        replace_name = self.input_replace_name.text()
        self.db.open()
        request = QSqlQuery(self.db)
        query = f"UPDATE events SET event_name = '{replace_name}' WHERE event_name = '{input_name}'"
        request.exec(query)
        self.db.close()

    def r_date_btn_click(self):
        input_name = self.input_replace_box.currentText()
        replace_date = self.input_replace_date.date()
        replace_date = replace_date.toString("dd.MM.yyyy")
        self.db.open()
        request = QSqlQuery(self.db)
        query = f"UPDATE events SET event_date = '{replace_date}' WHERE event_name = '{input_name}'"
        request.exec(query)
        self.db.close()

    def r_time_btn_click(self):
        input_name = self.input_replace_box.currentText()
        replace_time = self.input_replace_time.time()
        replace_time = replace_time.toString("hh:mm")
        self.db.open()
        request = QSqlQuery(self.db)
        query = f"UPDATE events SET event_time = '{replace_time}' WHERE event_name = '{input_name}'"
        request.exec(query)
        self.db.close()

    def r_geo_btn_click(self):
        input_name = self.input_replace_box.currentText()
        replace_geo = self.input_replace_geo.text()
        self.db.open()
        request = QSqlQuery(self.db)
        query = f"UPDATE events SET event_geo = '{replace_geo}' WHERE event_name = '{input_name}'"
        request.exec(query)
        self.db.close()

    def d_btn_click(self):
        input_name = self.input_delete_name.currentText()
        self.db.open()
        request = QSqlQuery(self.db)
        query = f"DELETE from events WHERE event_name = {input_name}"
        request.exec(query)
        self.db.close()

    def fill_lst(self):
        self.db.open()
        query = QSqlQuery("SELECT event_name FROM events")
        while query.next():
            self.input_replace_box.addItem(query.value(0))
            self.input_delete_name.addItem(query.value(0))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EventManager()
    ex.show()
    sys.exit(app.exec())