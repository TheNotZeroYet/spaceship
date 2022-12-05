import pygame as pg


class Holder:
    def __init__(self, x, y, font, font_size, font_color, text, score):
        self.x = x
        self.y = y
        self.color = font_color
        self.text = text
        self.score = score
        self.font = pg.font.Font(font, font_size)

    def set_score(self, score):
        self.score = score

    def get_text(self):
        return self.font.render(self.text + ": " + str(self.score), True, self.color)

    def update(self, screen):
        screen.blit(self.get_text(), (self.x, self.y))
