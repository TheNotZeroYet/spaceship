import pygame as pg


class Screen:
    WIDTH = 1200
    HEIGHT = 800
    FPS = 120

    def __init__(self, img):
        self.img = pg.transform.scale(img, (Screen.WIDTH, Screen.HEIGHT))
        self.is_game = False

    def set_game(self, flag):
        self.is_game = flag

    def set_img(self, img):
        self.img = pg.transform.scale(img, (Screen.WIDTH, Screen.HEIGHT))

    def update(self, screen):
        screen.blit(self.img, (0, 0))