import pygame as pg


class Screen:
    WIDTH = 1200
    HEIGHT = 800
    FPS = 120

    def __init__(self, back_img, fail_img):
        self.back_img = pg.transform.scale(back_img, (Screen.WIDTH, Screen.HEIGHT))
        self.fail_img = pg.transform.scale(fail_img, (Screen.WIDTH, Screen.HEIGHT))
        self.is_game = False

    def set_game(self, flag):
        self.is_game = flag

    def current_img(self):
        if self.is_game:
            return self.back_img
        return self.fail_img

    def update(self, screen):
        screen.blit(self.current_img(), (0, 0))