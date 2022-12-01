import pygame as pg
from random import randint

from meteor import Meteor
from screen import Screen

pg.init()


class Spaceship:
    # SPEED = 5
    SIZE = 100

    def __init__(self, img_list, x):
        self.img_list = [pg.transform.scale(img, (Spaceship.SIZE, Spaceship.SIZE)) for img in img_list]
        self.img = self.img_list[0]
        self.over_y = randint(0, 400)
        self.x = x
        self.y = Screen.HEIGHT - Spaceship.SIZE - self.over_y
        self.life = 0
        self.is_big_size = False
        self.speed = randint(2, 7)

    def set_size(self, size):
        self.img_list = [pg.transform.scale(img, (Spaceship.SIZE, Spaceship.SIZE)) for img in self.img_list]
        self.img = self.img_list[self.life]


    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x <= Screen.WIDTH - Spaceship.SIZE:
            self.x += self.speed

    def collision(self, meteor):
        if self.x - Spaceship.SIZE <= meteor.x <= self.x + Spaceship.SIZE and self.y <= meteor.y + meteor.size <= self.y + Spaceship.SIZE + meteor.size:
            return True
        return False

    def set_img_by_life(self):
        self.img = self.img_list[self.life]

    def life_edit(self, count):
        self.life += count
        self.set_img_by_life()

    def update(self, screen):
        screen.blit(self.img, (self.x, self.y))





