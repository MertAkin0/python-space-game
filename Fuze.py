import pygame
import os.path

klasor = os.path.dirname(__file__)
resimKlasoru = os.path.join(klasor, "resimler")

fire = pygame.image.load(os.path.join(resimKlasoru, "laser.png"))

width = 1024


class Fuze(pygame.sprite.Sprite):
    def __init__(self, parcay):
        super().__init__()
        self.image = fire
        # self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = parcay + 20

    def update(self, *args):
        self.rect.x += 15

        if self.rect.left > width:
            self.kill()
