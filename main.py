import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
running = True
clock = pygame.time.Clock()
dt = 0  # Initialize dt

awal_x = 10
awal_y = 10
awal_x2 = 490
awal_y2 = 490

ball_pos = pygame.Vector2(400,400)
speed = pygame.Vector2(5, 5)
black = 0, 0, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)  # Clear the screen with black

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and awal_y > 0:
        awal_y -= 300 * dt  # Move the line up
    if keys[pygame.K_s] and awal_y < screen.get_height() - 100:
        awal_y += 300 * dt  # Move the line down
    if keys[pygame.K_p] and awal_y2 > 0:
        awal_y2 -= 300 * dt  # Move the line up
    if keys[pygame.K_l] and awal_y2 < screen.get_height() - 100:
        awal_y2 += 300 * dt  # Move the line down

    pygame.draw.line(screen, (255, 0, 0), (awal_x, awal_y), (awal_x, awal_y + 90), 12)
    pygame.draw.line(screen, (255, 0, 0), (awal_x2, awal_y2), (awal_x2, awal_y2 - 90), 12)

    ball_pos += speed
    if ball_pos.x < 0 or ball_pos.x > 500:
        speed.x = -speed.x
    if ball_pos.y < 0 or ball_pos.y > 500:
        speed.y = -speed.y

    # Check collision with the lines
    if awal_x - 10 < ball_pos.x < awal_x + 10 and awal_y < ball_pos.y < awal_y + 90:
        speed.x = -speed.x
    if awal_x2 - 10 < ball_pos.x < awal_x2 + 10 and awal_y2 - 90 < ball_pos.y < awal_y2:
        speed.x = -speed.x

    pygame.draw.circle(screen, (255, 0, 0), (int(ball_pos.x), int(ball_pos.y)), 10)

    pygame.display.flip()  # Update the display

    dt = clock.tick(60) / 1000  # Update dt

pygame.quit()
