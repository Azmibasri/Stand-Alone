import pygame

def initialize_pygame():
    pygame.init()
    pygame.display.set_caption("Stand Alone 0.0.2")
    icon = pygame.image.load("Image/UI/Icon.jpeg")
    pygame.display.set_icon(icon)
    return pygame.display.set_mode((500, 500)), pygame.time.Clock(), pygame.display.Info()

def load_assets():
    knight = pygame.image.load("Image/character/knight.png")
    return pygame.transform.scale(knight, (100, 100))
