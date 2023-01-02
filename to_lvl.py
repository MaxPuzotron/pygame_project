import PyQt5
import sqlite3
import sys
import os

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from in_game_window_lvl1 import Game_window


class To_lvl(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/to_lvl.ui", self)
        self.to_lvl1_button.clicked.connect(self.to_lvl1)
        self.to_lvl2_button.clicked.connect(self.to_lvl2)

    def to_lvl1(self):
        shahid.show()
        QMainWindow.close(self)

    def to_lvl2(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = To_lvl()
    ex.show()
    shahid = Game_window()
    sys.exit(app.exec_())
