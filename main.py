import arcade as koshak
import math
import time
import base
import nuggets
from constants import *
from koshak import *
from milk import *
from nuggets import *


class Game(koshak.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # textures
        self.bg = koshak.load_texture("background.png")

        # sprites
        self.koshak_nash = Koshak_nash(self)
        self.nasha_baza = base.Base("cat base.png", self)
        self.vrag_baza = base.Base("MCDONALDS.png", self)

        # fields
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.active = True
        self.result = "run"

        # sprite lists
        self.milks = koshak.SpriteList()
        self.fries = koshak.SpriteList()
        self.nuggets = []

    def setup(self):
        self.koshak_nash.center_x = 90
        self.koshak_nash.center_y = 190
        self.nasha_baza.center_x = 165
        self.nasha_baza.center_y = 350
        self.vrag_baza.center_x = 1035
        self.vrag_baza.center_y = 350
        for i in range(1, 4):
            nugget = Nuggets(self)
            nugget.center_x = 800
            nugget.center_y = 200 * i - 50
            self.nuggets.append(nugget)

    def update(self, delta_time: float):
        if self.active == True:
            nuggets_destroyed = 0
            self.koshak_nash.update()
            self.milks.update()
            self.fries.update()
            self.nasha_baza.update()
            self.vrag_baza.update()
            for nugget in self.nuggets:
                nugget.update()
                if nugget.shots >= 5:
                    nuggets_destroyed += 1
            if nuggets_destroyed == 3 or self.vrag_baza.shots >= 10:
                self.active = False
                self.result = "win"
            if self.koshak_nash.shots >= 5 or self.nasha_baza.shots >= 10:
                self.active = False
                self.result = "lose"

    def on_draw(self):
        self.clear((255, 255, 255))
        koshak.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.koshak_nash.draw()
        self.milks.draw()
        self.fries.draw()
        self.nasha_baza.draw()
        if self.result == "lose":
            koshak.draw_text(300, SCREEN_HEIGHT / 2, (0, 255, 0), 74)
        self.vrag_baza.draw()
        for nugget in self.nuggets:
            nugget.draw()
        if self.result == "win":
            koshak.draw_text("YOU WIN", "YOU LOSE", 300, SCREEN_HEIGHT / 2, (255, 0, 0), 74)
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == koshak.key.A:
            self.koshak_nash.change_angle = 2.5
            self.left_pressed = True
            self.right_pressed = False

        if symbol == koshak.key.D:
            self.koshak_nash.change_angle = -2.5
            self.right_pressed = True
            self.left_pressed = False

        if symbol == koshak.key.W:
            self.koshak_nash.change_x = 4
            self.koshak_nash.change_y = 4
            self.up_pressed = True
            self.down_pressed = False

        if symbol == koshak.key.S:
            self.koshak_nash.change_x = -3
            self.koshak_nash.change_y = -3
            self.down_pressed = True
            self.up_pressed = False

        if symbol == koshak.key.SPACE:
            milk = Milk("milk.png", self.koshak_nash, "koshak")
            self.milks.append(milk)
            print(self.koshak_nash.angle)


    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == koshak.key.A and not self.right_pressed:
            self.koshak_nash.change_angle = 0

        if symbol == koshak.key.D and not self.left_pressed:
            self.koshak_nash.change_angle = 0

        if symbol == koshak.key.W and not self.down_pressed:
            self.koshak_nash.change_x = 0
            self.koshak_nash.change_y = 0

        if symbol == koshak.key.S and not self.up_pressed:
            self.koshak_nash.change_x = 0
            self.koshak_nash.change_y = 0


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Kashaki rulyat!")
game.setup()
koshak.run()
