#Pengaturan window
import pygame
pygame.init()
info = pygame.display.Info()
width, height = info.current_w, info.current_h
pygame.display.set_caption("Stand Alone 0.0.2")
icon = pygame.image.load("Image/UI/Icon.jpeg")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((500,500))
#Warna
white = (255,255,255)
red = (255,0,0)
#Game Running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    center_w = width / 2
    center_h = height / 2
    pygame.draw.line(screen,white,(0,480),(500,480),200)

    pygame.display.flip()
