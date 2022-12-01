from random import randint
import pygame as pg

from meteor import Meteor


class BonusMeteor(Meteor):

    def __init__(self, img_list):
        super().__init__(img_list)
        self.is_bonus = True
        self.random = randint(0, 2)
        if self.random == 0:
            self.bonus = "green"
        elif self.random == 1:
            self.bonus = "red"
        else:
            self.bonus = "purple"
        self.img = pg.transform.scale(img_list[self.random], (self.size, self.size))