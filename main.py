import pygame
import sys
from init import initialize_pygame, load_assets
from logic import handle_events, update_logic
from draw import draw_elements

def main():
    screen, clock, info = initialize_pygame()
    scaled_image = load_assets()
    
    position = [0, 300]
    speed = 2
    is_jumping = False
    jump_height = 10
    jump_count = jump_height

    white = (255, 255, 255)
    black = (0, 0, 0)

    running = True
    while running:
        running = handle_events(running)
        keys = pygame.key.get_pressed()
        position, is_jumping, jump_count = update_logic(keys, position, speed, is_jumping, jump_height, jump_count)
        draw_elements(screen, white, black, position, scaled_image)
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
