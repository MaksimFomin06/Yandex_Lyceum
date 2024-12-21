import io
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>425</width>
    <height>243</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>50</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Рассчитать</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="filenameEdit">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>50</y>
      <width>131</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="maxEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>90</y>
      <width>141</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Максимальное значение:</string>
    </property>
   </widget>
   <widget class="QLabel" name="minEdit">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>120</y>
      <width>131</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Минимальное значение:</string>
    </property>
   </widget>
   <widget class="QLabel" name="avgEdit">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>150</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Среднее значение:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>81</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя файла</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>90</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_2">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>120</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit_3">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>150</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>425</width>
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


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 250)
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.button.clicked.connect(self.calculate_stats)

    def calculate_stats(self):
        filename = self.filenameEdit.text()
        try:
            with open(f"{filename}", 'r') as file:
                numbers = []
                for line in file:
                    try:
                        number = float(line.strip())
                        numbers.append(number)
                    except ValueError:
                        pass

                if not numbers:
                    self.statusBar().showMessage('Файл пустой или содержит неверные данные')
                    return

                max_value = max(numbers)
                min_value = min(numbers)
                avg_value = round(sum(numbers) / len(numbers), 2)

                self.lineEdit.setText(str(max_value))
                self.lineEdit_2.setText(str(min_value))
                self.lineEdit_3.setText(str(avg_value))

        except FileNotFoundError:
            self.statusBar().showMessage(f'Файл {filename} не найден')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileStat()
    window.show()
    sys.exit(app.exec())