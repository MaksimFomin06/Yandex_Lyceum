import io
import sys
from PyQt6 import uic

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QTableView


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>661</width>
    <height>476</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QTableView" name="view">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>621</width>
     <height>421</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class HomeWork(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUi()

    def initUi(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("coffee.sqlite")
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable("coffee")
        model.select()

        self.view.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = HomeWork()
    ex.show()
    sys.exit(app.exec())