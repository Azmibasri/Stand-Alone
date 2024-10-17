import pygame

def handle_events(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running

def update_logic(keys, position, speed, is_jumping, jump_height, jump_count):
    if keys[pygame.K_a]:
        position[0] -= speed
    if keys[pygame.K_d]:
        position[0] += speed
    
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
            
    return position, is_jumping, jump_count
