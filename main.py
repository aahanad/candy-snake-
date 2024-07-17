import pygame
import random
pygame.init()
WIDTH=850
HEIGHT=900
screen=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("C:\Aahana\candy snake code\Background.PNG")
bg=pygame.transform.scale(bg,(1500,900))
game=True
bg_x=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(bg,(bg_x,0))
    bg_x=bg_x-0.7
    if abs(bg_x)>500:
        bg_x=0
    pygame.display.update()