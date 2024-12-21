import io
import sys

from PyQt6 import uic
from random import choice
from PyQt6.QtWidgets import QMainWindow, QApplication

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>366</width>
    <height>147</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>30</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Получить</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="text_field">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>20</y>
      <width>251</width>
      <height>71</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>366</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class RandomString(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 100)
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.button.clicked.connect(self.quest)
    def quest(self):
        with open("lesson_7/lines.txt", "r") as f:
            lines = f.read().splitlines()
            if len(lines) > 0:
                random_line = choice(lines).strip()
                self.text_field.setText(f"{random_line}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = RandomString()
    ex.show()
    sys.exit(app.exec())