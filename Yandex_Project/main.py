import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDateEdit, QTimeEdit
from PyQt6.QtSql import QSqlDatabase, QSqlQuery


class EventManager(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design/design.ui", self)
        self.init_ui()

    def init_ui(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data/EventManager_db.sqlite")

        self.fill_list()
        self.label_error.hide()
        self.label_delete_text.hide()
        self.label_none_text.hide()
        self.label_name_error.hide()

        self.AddButton.clicked.connect(self.add_btn_click)
        self.replaceNameButton.clicked.connect(lambda: self.update_field("event_name", "name"))
        self.replaceDateButton.clicked.connect(lambda: self.update_field("event_date", "date"))
        self.replaceTimeButton.clicked.connect(lambda: self.update_field("event_time", "time"))
        self.replaceGeoButton.clicked.connect(lambda: self.update_field("event_geo", "geo"))
        self.DeleteButton.clicked.connect(self.delete_event)
        
    def add_btn_click(self):
        self.db.open()
        input_name = self.input_name.text().strip()
        input_date = self.input_date.date().toString("dd.MM.yyyy")
        input_time = self.input_time.time().toString("hh:mm")
        input_geo = self.input_geo.text().strip()

        request = QSqlQuery(self.db)
        query = f"SELECT event_name FROM events WHERE event_name = '{input_name}'"
        request.exec(query)

        if not all([input_name, input_date, input_time, input_geo]):
            self.label_error.show()
        elif request.first():
            self.label_error.hide()
            self.label_name_error.show()
            self.db.close()
            return
        else:
            self.label_name_error.hide()
            self.label_error.hide()
            query = f"INSERT INTO events VALUES ('{input_name}', '{input_date}', '{input_time}', '{input_geo}')"
            request.exec(query)
        self.db.close()
        self.update()

    def update_field(self, field, param):
        input_name = self.input_replace_box.currentText()
        new_value = getattr(self, f"input_replace_{param}").text().strip()
        if not new_value:
            self.label_error.show()
            return
        self.label_error.hide()
        self.db.open()
        request = QSqlQuery(self.db)
        query = f"UPDATE events SET {field} = '{new_value}' WHERE event_name = '{input_name}'"
        request.exec(query)
        self.db.close()
        self.update()

    def delete_event(self):
        input_name = self.input_delete_name.currentText()
        self.db.open()
        if not input_name:
            self.label_none_text.show()
        request = QSqlQuery(self.db)
        query = f"DELETE FROM events WHERE event_name = '{input_name}'"
        self.label_delete_text.show()
        request.exec(query)
        self.db.close()
        self.update()

    def fill_list(self):
        self.db.open()
        query = QSqlQuery("SELECT event_name FROM events")
        while query.next():
            self.input_replace_box.addItem(query.value(0))
            self.input_delete_name.addItem(query.value(0))

    def update(self):
        self.input_replace_box.clear()
        self.input_delete_name.clear()
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