import pygame as pg


class Button:
    HEIGHT = 100
    WIDTH = 200

    def __init__(self, x, y, btn_img):
        self.img = pg.transform.scale(btn_img, (Button.WIDTH, Button.HEIGHT))
        self.x = x - Button.WIDTH / 2
        self.y = y - Button.HEIGHT / 2

    def update(self, screen):
        screen.blit(self.img, (self.x, self.y))
