import arcade as koshak
import math
import time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700


class Game(koshak.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        pass

    def update(self, delta_time: float):
        pass

    def on_draw(self):
        self.clear((255, 255, 255))


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Kashaki rulyat!")
koshak.run()