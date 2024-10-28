import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>630</width>
    <height>512</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Антиплагиат v0.0001</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>631</width>
      <height>461</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="2" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Текст 1</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Текст 2</string>
       </property>
      </widget>
     </item>
     <item row="0" column="1">
      <widget class="QDoubleSpinBox" name="alert_value"/>
     </item>
     <item row="0" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Порог срабатывания (%)</string>
       </property>
      </widget>
     </item>
     <item row="3" column="0">
      <widget class="QPlainTextEdit" name="text1"/>
     </item>
     <item row="3" column="1">
      <widget class="QPlainTextEdit" name="text2"/>
     </item>
     <item row="4" column="0" colspan="2">
      <widget class="QPushButton" name="checkBtn">
       <property name="text">
        <string>Сравнить</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>630</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar">
   <property name="font">
    <font>
     <pointsize>15</pointsize>
    </font>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.checkBtn.clicked.connect(self.f)

    def f(self):
        doorstep = (self.alert_value.value())

        text1, text2 = self.text1.toPlainText().strip().split('\n'), self.text2.toPlainText().strip().split('\n')

        percent = round(100 * len(set(text1) & set(text2)) / len(set(text1) | set(text2)), 2)


        if percent >= doorstep:
            self.statusbar.showMessage(f'Тексты похожи на {percent:.2f}%, плагиат')
        else:
            self.statusbar.showMessage(f'Тексты похожи на {percent:.2f}%, не плагиат')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec())
