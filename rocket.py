import pygame as pg
from random import choice

from screen import Screen

pg.init()


class Rocket:
    SPEED = 5
    HEIGHT = 45
    WIDTH = 25

    def __init__(self, img, img_enemy, side, x, y):
        self.side = side
        self.size = 35

        if side == "up":
            self.img = pg.transform.scale(img, (Rocket.WIDTH, Rocket.HEIGHT))
            self.x = choice([x, x + 70])
            self.y = y
        else:
            self.img = pg.transform.scale(img_enemy, (Rocket.WIDTH, Rocket.HEIGHT))
            self.x = x + 70
            self.y = y + 30
        self.is_active = True

    def move_up(self):
        if self.y >= 0:
            self.y -= Rocket.SPEED
        else:
            self.is_active = False

    def move_down(self):
        if self.y <= Screen.HEIGHT:
            self.y += Rocket.SPEED
        else:
            self.is_active = False

    def collision(self, meteor):
        if self.x - 50 <= meteor.x <= self.x + 50 and self.y - 50 <= meteor.y <= self.y + 50:
            return True
        return False

    def update(self, screen):
        if self.side == "up":
            self.move_up()
        else:
            self.move_down()
        screen.blit(self.img, (self.x, self.y))
