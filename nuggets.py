import arcade as koshak
import math
import time
import milk
from constants import *


class Nuggets(koshak.Sprite):
    def __init__(self, game):
        super().__init__("nugget.png", 0.2, flipped_horizontally=True, flipped_vertically=True)
        self.active = True
        self.game = game
        self.fries_spawn_time = time.time()

        self.shots = 0

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super().draw()
        koshak.draw_rectangle_outline(self.center_x, self.center_y + 55, 50, 15, (255, 255, 255))
        damage = self.shots * 10
        koshak.draw_rectangle_filled(self.center_x - damage / 2, self.center_y + 55, 50 - damage, 13, (205, 50, 50))

    def update(self):
        hits = koshak.check_for_collision_with_list(self, self.game.milks)
        for i in hits:
            if i.side == "koshak":
                i.kill()
                self.shots += 1

        if self.shots >= 5:
            self.active = False
            self.angle = -90
            self.shots = 5

        if self.active == True:
            radius = koshak.get_distance_between_sprites(self, self.game.koshak_nash)
            radius_base = koshak.get_distance_between_sprites(self, self.game.nasha_baza)
            watch = 0
            if 0 < watch < 40:
                self.angle = watch
                self.texture = koshak.load_texture("nugget.png", flipped_horizontally= True)
            elif 0 < watch < 400:
                self.angle = watch
                self.texture = koshak.load_texture("nugget.png", flipped_horizontally= True, flipped_vertically= True)

            if radius <= 400:
                delta_x = self.game.koshak_nash.center_x - self.center_x
                delta_y = self.game.koshak_nash.center_y - self.center_y
                self.fire(delta_x, delta_y)
            elif radius_base <= 400:
                delta_x = self.game.nasha_baza.center_x - self.center_x
                delta_y = self.game.nasha_baza.center_y - self.center_y
                self.fire(delta_x, delta_y)
            else:
                self.angle = 180
                self.center_x -= 1
    def fire(self, delta_x, delta_y):
        self.angle = math.degrees(math.atan2(delta_y, delta_x))
        if time.time() - self.fries_spawn_time > 2:
            self.part_x = math.cos(math.radians(self.angle))
            self.part_y = math.sin(math.radians(self.angle))
            fries = milk.Milk("fries_rb.png", self, "nuggets", True)
            self.fries_spawn_time = time.time()
            self.game.fries.append(fries)

