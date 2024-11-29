
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QDateEdit, QTimeEdit, QTableWidgetItem, QHeaderView
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtCore import Qt


class EventManager(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design/design.ui", self)
        self.setWindowTitle("Event Manager")
        self.initUi()

    def initUi(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data/EventManager_db.sqlite")

        self.fill_list()
        self.fill_db()

        self.AddButton.clicked.connect(self.add_btn_click)
        self.replaceNameButton.clicked.connect(lambda: self.update_field("event_name", "name"))
        self.replaceDateButton.clicked.connect(lambda: self.update_field("event_date", "date"))
        self.replaceTimeButton.clicked.connect(lambda: self.update_field("event_time", "time"))
        self.replaceGeoButton.clicked.connect(lambda: self.update_field("event_geo", "geo"))
        self.DeleteButton.clicked.connect(self.delete_event)

        self.add_div_texts = ["Ошибка: Заполните все поля",
                              "Ошибка: Запись с таким названием уже существует",
                              "Запись добавлена"]
        self.replace_div_texts = ["Поле не может быть пустым",
                                  "Запись изменена"]
        self.delete_div_texts = ["Ничего не найдено",
                                 "Запись удалена"]
    
    def fill_db(self):
        self.events_db.clearContents()
        self.events_db.setRowCount(0)
        self.db.open()
        self.events_db.setColumnCount(4)
        self.events_db.setHorizontalHeaderLabels(["Название", "Дата", "Время", "Место"])

        query = QSqlQuery("SELECT event_name, event_date, event_time, event_geo FROM events")
        row = 0
        while query.next():
            self.events_db.insertRow(row)
            name = QTableWidgetItem(query.value(0))
            date = QTableWidgetItem(query.value(1))
            time = QTableWidgetItem(query.value(2))
            geo = QTableWidgetItem(query.value(3))

            for item in [name, date, time, geo]:
                item.setTextAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)

            self.events_db.setItem(row, 0, name)
            self.events_db.setItem(row, 1, date)
            self.events_db.setItem(row, 2, time)
            self.events_db.setItem(row, 3, geo)

            self.events_db.resizeRowsToContents()
            header = self.events_db.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents.Stretch)
            
            row += 1
        
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
            self.label_add_notification.setText(self.add_div_texts[0])
        elif request.first():
            self.label_add_notification.setText(self.add_div_texts[1])
        else:
            query = f"INSERT INTO events VALUES ('{input_name}', '{input_date}', '{input_time}', '{input_geo}')"
            request.exec(query)
            self.label_add_notification.setText(self.add_div_texts[2])
        self.db.close()
        self.update()
        
    def update_field(self, field, param):
        input_name = self.input_replace_box.currentText()
        request = QSqlQuery(self.db)
        self.db.open()
        
        if not input_name:
            self.label_replace_notification.setText(self.replace_div_texts[0])
        else:
            new_value = getattr(self, f"input_replace_{param}").text().strip()
            if not new_value:
                self.label_replace_notification.setText(self.replace_div_texts[0])
            query = f"SELECT event_name FROM events WHERE event_name = '{new_value}'"
            request.exec(query)
            if request.first():
                self.label_replace_notification.setText(self.add_div_texts[1])
            else:
                query = f"UPDATE events SET {field} = '{new_value}' WHERE event_name = '{input_name}'"
                request.exec(query)
                self.label_replace_notification.setText(self.replace_div_texts[1])
        self.db.close()
        self.update()

    def delete_event(self):
        input_name = self.input_delete_name.currentText()
        self.db.open()
        request = QSqlQuery(self.db)
        if not input_name:
            self.label_delete_notificatoin.setText(self.delete_div_texts[0])
        else:
            query = f"DELETE FROM events WHERE event_name = '{input_name}'"
            request.exec(query)
            self.label_delete_notificatoin.setText(self.delete_div_texts[1])
        self.db.close()
        self.update()

    def fill_list(self):
        self.db.open()
        query = QSqlQuery("SELECT event_name FROM events")
        while query.next():
            self.input_replace_box.addItem(query.value(0))
            self.input_delete_name.addItem(query.value(0))

    def update(self):
        self.fill_db()
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