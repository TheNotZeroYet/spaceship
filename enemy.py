import pygame as pg
from random import randint, random

from screen import Screen


class Enemy:
    SIZE = 150

    def __init__(self, img):
        self.img = pg.transform.scale(img, (Enemy.SIZE, Enemy.SIZE))
        self.x = randint(0, Screen.WIDTH - Enemy.SIZE)
        self.y = 0
        self.is_active = True
        self.is_move_y = True
        self.border_y = randint(0, 300)
        self.speed_x = random()
        self.speed_y = random()


    def move_down(self):
        if self.y <= Screen.HEIGHT // 2 - Enemy.SIZE - self.border_y:
            self.y += self.speed_y
        else:
            self.is_move_y = False

    def collision_spaceship_rocket(self, enemy):
        if self.x - 50 <= enemy.x <= self.x + 50 and self.y - 50 <= enemy.y <= self.y + 50:
            return True
        return False

    def move_left(self):
        self.x -= self.speed_x

    def move_right(self):
        self.x += self.speed_x

    def update(self, screen, ship_x):
        if self.is_move_y:
            self.move_down()

        if self.x >= ship_x:
            self.move_left()
        else:
            self.move_right()

        screen.blit(self.img, (self.x, self.y))