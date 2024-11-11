import arcade as koshak

import milk


class Base(koshak.Sprite):
    def __init__(self, image, game):
        super().__init__(image, 0.7)

        self.shots = 0
        self.game = game

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super().draw()
        koshak.draw_rectangle_outline(self.center_x, self.center_y + 320, 250, 15, (0, 0, 0), 3)
        damage = self.shots * 25
        koshak.draw_rectangle_filled(self.center_x - damage / 2, self.center_y + 320, 250 - damage, 9,
                                     koshak.color.GREEN)

    def update(self):
        hits = koshak.check_for_collision_with_list(self, self.game.milks)
        for i in hits:
            i.kill()
            self.shots += 1