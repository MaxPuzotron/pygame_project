import PyQt5
import sqlite3
import sys
import os
import game

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Game_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/in_game_window.ui", self)
        self.textEdit.setReadOnly(True)
        self.choise1_text.setReadOnly(True)
        self.choise2_text.setReadOnly(True)
        self.choise1.clicked.connect(self.get_new_text)
        self.choise2.clicked.connect(self.get_new_text)
        self.initial_text.clicked.connect(self.get_initial_text)
        global i
        global a
        global b
        global c
        i = 0
        b = 'subtext2' + str(i)
        c = 'subtext1' + str(i)
        a = 'text' + str(i)
        print(c)
        print(a)
        print(b)

    def get_text(self):
        f = open(f'texts for lvl1/text0', 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
            self.textEdit.setReadOnly(True)

    def get_new_text(self):
        global i
        global a
        global b
        global c
        f = open(f'texts for lvl1/{a}', 'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
            self.textEdit.setReadOnly(True)
        f = open(f'texts for lvl1/{b}', 'r')
        with f:
            data = f.read()
            self.choise2_text.setText(data)
            self.textEdit.setReadOnly(True)
        f = open(f'texts for lvl1/{c}', 'r')
        with f:
            data = f.read()
            self.choise1_text.setText(data)
            self.textEdit.setReadOnly(True)
        a = a[:4]
        b = b[:8]
        c = c[:8]
        print(c)
        print(a)
        print(b)
        if i < 1:
            i += 1
        a = a + str(i)
        b = b + str(i)
        c = c + str(i)
        print(a)
        print(b)
        print(c)

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
        result = cur.execute(f"""UPDATE parametres 
                SET value = '90'
                WHERE name = health
                            """).fetchall()
        print(result)
        con.commit()
        self.health_bar.setText(result)


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
