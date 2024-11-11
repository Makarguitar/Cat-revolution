from constants import *
import arcade as koshak
import math


class Koshak_nash(koshak.Sprite):
    def __init__(self, game):
        super().__init__("koshak.png", 0.12)
        self.active = True
        self.shots = 0
        self.game = game

    def update(self):
        if self.active:
            self.angle += self.change_angle
            self.part_x = math.cos(math.radians(self.angle))
            self.part_y = math.sin(math.radians(self.angle))
            self.center_x += self.part_x * self.change_x
            self.center_y += self.part_y * self.change_y

        if self.bottom < 0:
            self.bottom = 0

        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT

        if self.left < 0:
            self.left = 0

        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        hits = koshak.check_for_collision_with_list(self, self.game.fries)

        for i in hits:
            if i.side == "nuggets":
                i.kill()
                self.shots += 1
            print("test")

        if self.shots >= 5:
            self.angle = 90
            self.shots = 5
            self.active = False


    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super().draw()
        koshak.draw_rectangle_outline(self.center_x, self.center_y + 50, 50, 15, (255, 255, 255), 1)
        damage = self.shots * 10
        koshak.draw_rectangle_filled(self.center_x - damage / 2, self.center_y + 50, 50 - damage, 13, (50, 205, 50))