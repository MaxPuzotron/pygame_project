import PyQt5
import sqlite3
import sys
import os

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Game_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/in_game_window.ui", self)
        self.textEdit.setReadOnly(True)
        self.new_text.clicked.connect(self.get_new_text)
        self.initial_text.clicked.connect(self.get_initial_text)
        global i
        global a
        i = 0
        a = 'text' + str(i)
        print(a)

    def get_new_text(self):
        global i
        global a
        f = open(f'texts for lvl1/{a}', 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
            self.textEdit.setReadOnly(True)
        a = a[:4]
        print(a)
        if i < 1:
            i += 1
        a = a + str(i)
        print(a)

    def get_initial_text(self):
        global i
        global a
        f = open(f'texts for lvl1/{a}', 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
            self.textEdit.setReadOnly(True)
        a = a[:4]
        if i < 1:
            i -= 1
        a = a + str(0)

    def health(self):
        con = sqlite3.connect("parametres.db")
        cur = con.cursor()
        a = self.health_bar.toPlainText()
        result = cur.execute(f"""UPDATE parametres 
                SET value = '90'
                WHERE name = health
                            """)
        con.commit()

    def money(self):
        con = sqlite3.connect("parametres.db")
        cur = con.cursor()
        a = self.money_bar.toPlainText()
        result = cur.execute(f"""UPDATE parametres 
                SET value = '20'
                WHERE name = money
                            """)
        con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game_window()
    ex.show()
    sys.exit(app.exec_())
