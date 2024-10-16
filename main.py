#Pengaturan window
import pygame
pygame.init()
info = pygame.display.Info()
width, height = info.current_w, info.current_h
pygame.display.set_caption("Stand Alone 0.0.2")
icon = pygame.image.load("Image/UI/Icon.jpeg")
knight = pygame.image.load("Image\character\knight.png")
scaled_image = pygame.transform.scale(knight, (100, 100))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((500,500))
position = [0, 300]
#Pengaturan karakter
speed = 0.5
is_jumping = False
jump_height = 10
jump_count = jump_height

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
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        position[0] -= speed
    if keys[pygame.K_d]:
        position[0] += speed
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            pygame.display.flip()
    else:
        if jump_count >= -jump_height:
            neg = 1 if jump_count > 0 else -1
            position[1] -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
            pygame.display.flip()
        else:
            is_jumping = False
            jump_count = jump_height
            pygame.display.flip()

    screen.blit(scaled_image,position)
    pygame.display.flip()
