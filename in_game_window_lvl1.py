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
        uic.loadUi("ui files/in_game_windowlvl1.ui", self)
        self.textEdit.setReadOnly(True)
        self.choise1_text.setReadOnly(True)
        self.choise2_text.setReadOnly(True)
        self.choise1.clicked.connect(self.get_text_to_left)
        self.choise2.clicked.connect(self.get_text_to_right)
        self.initial_text.clicked.connect(self.get_text)
        self.update_score()
        global right_button
        global left_button
        global i
        global a
        global b
        global c
        left_button = 0
        right_button = 0
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
        self.choise2_text.setText('')
        self.choise1_text.setText('')

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

    def get_text_to_right(self):
        self.get_new_text()
        #self.proverka_right()
        global right_button
        right_button = 1
        print(right_button)

    def proverka_right(self):
        if 1 == 1:
            self.add_money()
        if 0 == 0:
            self.sub_money()
        if 2 == 2:
            self.add_health()
        if 3 == 3:
            self.sub_health()

    def get_text_to_left(self):
        self.get_new_text()
        #self.proverka_left()
        global left_button
        left_button = 2
        print(left_button)

    def proverka_left(self):
        if 1 == 1:
            self.add_money()
        if 0 == 0:
            self.sub_money()
        if 2 == 2:
            self.add_health()
        if 3 == 3:
            self.sub_health()

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

    def add_money(self):
        pass

    def sub_money(self):
        pass

    def add_healph(self):
        pass

    def sub_health(self):
        pass

    def update_score(self):
        pass

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
