import pygame as pg
from random import randint, choice, random
from screen import Screen

class Meteor:
    def __init__(self, img_list):
        self.size = choice([30, 40, 50, 60, 70])
        self.img = pg.transform.scale(img_list[randint(0, len(img_list) - 1)], (self.size, self.size))
        self.speed = randint(1, 4)
        self.is_bonus = False
        self.x = randint(0, Screen.WIDTH - self.size)
        self.y = self.size
        self.is_active = True

    def move(self):
        if self.y < Screen.HEIGHT - self.size:
            self.y += self.speed
        else:
            self.is_active = False

    def update(self, screen):
        self.move()
        screen.blit(self.img, (self.x, self.y))

