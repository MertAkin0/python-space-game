import pygame

ulti=0

def ultiCiz(pencere, x, y, deger):
    if deger < 0:
        deger = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = ulti
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(pencere, (255, 255, 255), outline_rect, 3)

    if deger > 60:
        pygame.draw.rect(pencere, (0, 255, 0), fill_rect)
    elif deger >= 30 and deger < 60:
        pygame.draw.rect(pencere, (204, 204, 0), fill_rect)
    elif deger < 30:
        pygame.draw.rect(pencere, (255, 0, 0), fill_rect)