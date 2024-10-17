import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Mendapatkan informasi layar
info = pygame.display.Info()
width, height = info.current_w, info.current_h

# Pengaturan jendela
pygame.display.set_caption("Stand Alone 0.0.2")
icon = pygame.image.load("Image/UI/Icon.jpeg")
knight = pygame.image.load("Image/character/knight.png")
scaled_image = pygame.transform.scale(knight, (100, 100))
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Pengaturan posisi awal karakter
position = [0, 300]

# Pengaturan karakter
speed = 2
is_jumping = False
jump_height = 10
jump_count = jump_height

# Warna
white = (255, 255, 255)
red = (255, 0, 0)
Black = (0,0,0)

# Game Running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Menggerakkan karakter
    if keys[pygame.K_a]:
        position[0] -= speed
    if keys[pygame.K_d]:
        position[0] += speed
    
    # Logika melompat
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -jump_height:
            neg = 1 if jump_count > 0 else -1
            position[1] -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = jump_height

    # Mengisi layar dengan warna putih
    screen.fill(Black)

    # Menggambar garis dasar
    pygame.draw.line(screen, white, (0, 480), (500, 480), 200)

    # Menggambar karakter di layar
    screen.blit(scaled_image, position)

    # Memperbarui tampilan
    pygame.display.flip()
    
    # Mengatur frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
