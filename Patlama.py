import pygame
import os.path


class Patlama(pygame.sprite.Sprite):
    def __init__(self, meteor, klasor, liste):
        super().__init__()
        self.meteor = meteor
        self.klasor = klasor
        self.liste = liste
        self.sayac = 1
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.klasor, self.liste[self.sayac])),
                                            self.meteor.image.get_size())
        self.rect = self.image.get_rect()
        self.rect.center = self.meteor.rect.center
        self.delay = 75
        self.sonDegisim = pygame.time.get_ticks()

    def update(self, *args):
        now = pygame.time.get_ticks()
        if now - self.sonDegisim > self.delay:
            self.sonDegisim = now
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(self.klasor, self.liste[self.sayac])),
                                                self.meteor.image.get_size())
            self.rect = self.image.get_rect()
            self.rect.center = self.meteor.rect.center
            self.sayac += 1

        if self.sayac == len(self.liste):
            self.kill()