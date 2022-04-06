import pygame
import os.path

klasor = os.path.dirname(__file__)
resimKlasoru = os.path.join(klasor, "resimler")

###Can Gorsel########
def canCiz(pencere, x, y, can):
    img = pygame.transform.scale(pygame.image.load(os.path.join(resimKlasoru, "ufo.png")), (20, 15))
    img_rect = img.get_rect()
    for i in range(can):
        img_rect.x = x + (40 * i)
        img_rect.y = y
        pencere.blit(img, img_rect)