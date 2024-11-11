import arcade

from constants import *
import arcade as koshak
from koshak import *


class Milk(koshak.Sprite):
    def __init__(self, image, koshak, side, is_flip_vertical = False):
        super().__init__(image, 0.1, flipped_vertically=is_flip_vertical)
        self.center_x = koshak.center_x
        self.center_y = koshak.center_y
        self.change_x = 12 * koshak.part_x
        self.change_y = 12 * koshak.part_y
        self.angle = koshak.angle
        self.side = side


    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left > SCREEN_WIDTH or self.right < 0 or self.top < 0 or self.bottom > SCREEN_HEIGHT:
            self.kill()
