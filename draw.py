import pygame

def draw_elements(screen, white, black, position, scaled_image):
    screen.fill(black)
    pygame.draw.line(screen, white, (0, 480), (500, 480), 200)
    screen.blit(scaled_image, position)
    pygame.display.flip()
