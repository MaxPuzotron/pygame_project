import PyQt5
import pygame
import random
import math
import sqlite3
import sys
import os

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from in_game_windowlvl2 import Game_window_lvl2
from in_game_window import Game_window
from pygame.locals import *


def gay_provoslavny_sex():
    run = 1
    while run == 1:
        winsize = [800, 600]
        black = [0, 0, 0]
        blue = [255, 255, 255]
        maxx = 780
        minx = 20
        maxy = 580
        miny = 0
        true = 1
        false = 0
        left = 1
        right = 0
        paddlestep = 4
        paddleleftxy = [5, 200]
        paddlerightxy = [775, 200]
        gameover = true
        ballxy = [200, 200]
        ballspeed = 2.3
        balldy = 1
        balldx = 1
        ballservice = true
        service = left
        scoreleft = 0
        scoreright = 0
        ballcludge = 0

        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(winsize)
        pygame.display.set_caption('Ping Pong')
        screen.fill(black)
        paddle = pygame.image.load('123/paddle.bmp').convert()
        paddleerase = pygame.image.load('123/erase.bmp').convert()
        ball = pygame.image.load('123/1.png').convert()
        ballerase = pygame.image.load('123/fireeraser.png').convert()

        while gameover == true:

            font = pygame.font.SysFont("Tahoma", 20)
            text_surface = font.render("Python Ping Pong", true, blue)
            screen.blit(text_surface, (80, 40))
            text_surface = font.render("For left paddle player please press A and Z to move.", true,
                                       blue)
            screen.blit(text_surface, (80, 120))
            text_surface = font.render("For right paddle player please press Up and Down to move.",
                                       true, blue)
            screen.blit(text_surface, (80, 160))
            text_surface = font.render("Press S to serve the ball", true, blue)
            screen.blit(text_surface, (80, 200))
            text_surface = font.render(
                "P to Pause, R to Resume, Press N to start a new game, and Q to Quit.", true, blue)
            screen.blit(text_surface, (80, 240))
            text_surface = font.render("You are now ready to play PyPong. Thank You! =)", true,
                                       blue)
            screen.blit(text_surface, (80, 280))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_n]:
                gameover = false
                screen.fill(black)
            elif pressed_keys[K_q]:
                run = 0
                exit()

            clock.tick(20)

        while not gameover:

            screen.blit(paddleerase, paddleleftxy)
            screen.blit(paddleerase, paddlerightxy)
            screen.blit(ballerase, ballxy)

            font = pygame.font.SysFont("Tahoma", 45)
            if scoreleft > 5 or scoreright > 5:
                gameover = True
            text_surface1 = font.render(str(scoreleft), true, blue)
            textleft = screen.blit(text_surface1, (40, 40))
            text_surface1 = font.render(str(scoreright), true, blue)
            textright = screen.blit(text_surface1, (700, 40))

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_a]:
                if paddleleftxy[1] > miny:
                    paddleleftxy[1] = paddleleftxy[1] - paddlestep
            elif pressed_keys[K_z]:
                if paddleleftxy[1] < maxy - 80:
                    paddleleftxy[1] = paddleleftxy[1] + paddlestep
            if pressed_keys[K_UP]:
                if paddlerightxy[1] > miny:
                    paddlerightxy[1] = paddlerightxy[1] - paddlestep
            elif pressed_keys[K_DOWN]:
                if paddlerightxy[1] < maxy - 80:
                    paddlerightxy[1] = paddlerightxy[1] + paddlestep

            if (pressed_keys[K_s] or pressed_keys[K_l]) and ballservice == true:
                ballservice = false
                if service == left:
                    balldx = random.randrange(2, 3)
                    balldy = random.randrange(-3, 3)
                    service = right
                else:
                    balldx = random.randrange(2, 3)
                    balldy = random.randrange(-3, 3)
                    service == left

            if pressed_keys[K_q]:
                run = 0
                exit()

            if pressed_keys[K_p]:
                gamepaused = true
                font = pygame.font.SysFont("Tahoma", 64)
                paused_surface = font.render("Paused", true, blue)
                paused_rect = screen.blit(paused_surface, (300, 250))
                pygame.display.update()

                while gamepaused == true:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                    pressed_keys = pygame.key.get_pressed()

                    if pressed_keys[K_r]:
                        gamepaused = false
                    clock.tick(20)

                pygame.draw.rect(screen, black, paused_rect)

            if ballservice is not true:
                if ballxy[0] < (paddleleftxy[0] + 20) and ballxy[1] > (paddleleftxy[1] - 18) and \
                        ballxy[1] < (paddleleftxy[1] + 98):
                    balldx = -balldx
                    if pressed_keys[K_z] or pressed_keys[K_x]:
                        balldy = random.randrange(2, 4)
                    else:
                        balldy = random.randrange(0, 3)
                elif ballxy[0] > (paddlerightxy[0] - 20) and ballxy[1] > (paddlerightxy[1] - 18) and \
                        ballxy[1] <= (paddlerightxy[1] + 98):
                    if ballcludge == 0:
                        balldx = -balldx
                        if pressed_keys[K_UP] or pressed_keys[K_DOWN]:
                            balldy = random.randrange(2, 4)
                        else:
                            balldy = random.randrange(0, 3)
                        ballcludge = 1
                    else:
                        ballcludge = ballcludge + 1
                        if ballcludge == 4:
                            ballcludge = 0

                elif ballxy[1] <= miny:
                    balldy = -balldy
                elif ballxy[1] >= maxy:
                    balldy = -balldy
                elif ballxy[0] <= minx:
                    ballservice = true
                    service = right
                    scoreright = scoreright + 1
                    pygame.draw.rect(screen, black, textright)
                elif ballxy[0] >= maxx:
                    ballservice = true
                    service = left
                    scoreleft = scoreleft + 1
                    pygame.draw.rect(screen, black, textleft)
                ballxy[0] = ballxy[0] + (ballspeed * balldx)
                ballxy[1] = ballxy[1] + (ballspeed * balldy)
            else:
                if service == left:
                    ballxy[0] = paddleleftxy[0] + 25
                    ballxy[1] = paddleleftxy[1] + 40
                elif service == right:
                    ballxy[0] = paddlerightxy[0] - 25
                    ballxy[1] = paddlerightxy[1] + 40

            screen.blit(paddle, paddleleftxy)
            screen.blit(paddle, paddlerightxy)
            screen.blit(ball, ballxy)
            pygame.display.update()

            clock.tick(100)

        while True:
            screen.fill([0, 0, 0])

            font = pygame.font.SysFont("Tahoma", 20)
            text_surface = font.render("Python Ping Pong", true, blue)
            screen.blit(text_surface, (80, 40))
            text_surface = font.render("For left paddle player please press A and Z to move.", true,
                                       blue)
            screen.blit(text_surface, (80, 120))
            text_surface = font.render("For right paddle player please press Up and Down to move.",
                                       true, blue)
            screen.blit(text_surface, (80, 160))
            text_surface = font.render("Press S to serve the ball", true, blue)
            screen.blit(text_surface, (80, 200))
            text_surface = font.render(
                "P to Pause, R to Resume, Press N to start a new game, and Q to Quit.", true, blue)
            screen.blit(text_surface, (80, 240))
            text_surface = font.render("You are now ready to play PyPong. Thank You! =)", true,
                                       blue)
            screen.blit(text_surface, (80, 280))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_n]:
                gameover = false
                screen.fill(black)
            elif pressed_keys[K_q]:
                run = 0
                exit()

            clock.tick(20)


class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/main_menu_window.ui", self)
        self.new_game_button.clicked.connect(self.open_new_game)
        self.close_button.clicked.connect(self.close)

    def close(self):
        QMainWindow.close(self)

    def open_new_game(self):
        shahid.show()
        QMainWindow.close(self)


class To_lvl(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui files/to_lvl.ui", self)
        self.to_lvl1_button.clicked.connect(self.to_lvl1)
        self.to_lvl2_button.clicked.connect(self.to_lvl2)

    def to_lvl1(self):
        alah.show()
        QMainWindow.close(self)

    def to_lvl2(self):
        QMainWindow.close(self)
        gay_provoslavny_sex()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    ex.show()
    shahid = To_lvl()
    kashmir = Game_window_lvl2()
    alah = Game_window()
    sys.exit(app.exec_())
