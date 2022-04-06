import pygame
import os.path
import sys

klasor = os.path.dirname(__file__)
resimKlasoru = os.path.join(klasor, "resimler")

width = 1024
height = 600

boyut = (width, height)

pencere = pygame.display.set_mode(boyut)
clock = pygame.time.Clock()


def show_gameover_screen():
    kontrol = True
    endstart = pygame.image.load(os.path.join(resimKlasoru, "endstart.png"))
    pencere.blit(endstart, endstart.get_rect())
    pygame.display.update()
    while kontrol:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    kontrol = False
