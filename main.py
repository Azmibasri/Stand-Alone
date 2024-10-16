#Pengaturan window
import pygame
pygame.init()
info = pygame.display.Info()
width, height = info.current_w, info.current_h
pygame.display.set_caption("Stand Alone 0.0.2")
icon = pygame.image.load("Image/UI/Icon.jpeg")
pygame.display.set_icon(icon)
pygame.display.set_mode((width,height-35))
#Game Running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False