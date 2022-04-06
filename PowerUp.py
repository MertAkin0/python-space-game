import pygame
import random
import os.path

klasor = os.path.dirname(__file__)
resimKlasoru = os.path.join(klasor, "resimler")

powerUps = ["can.png", "guclendirme.png", "guclendirme.png", "guclendirme.png", "guclendirme.png", "kalkan.png",
            "kalkan.png", "kalkan.png", "kalkan.png", "kalkan.png", "kalkan.png",
            "deguclendirme.png", "deguclendirme.png", "deguclendirme.png", "deguclendirme.png", "deguclendirme.png", ]


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.choice = random.choice(powerUps)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(resimKlasoru, self.choice)), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedX = 5

    def update(self, *args):
        self.rect.x -= self.speedX
