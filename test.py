import pygame

pygame.init()

screen_x = 600
screen_y = 400
player1 = pygame.Rect((30, 250, 10, 100))
player2 = pygame.Rect((550, 250, 10, 100))
boundary1 = pygame.Rect((0, 0, 600, 10))
boundary2 = pygame.Rect((0, 390, 600, 10))
border1 = pygame.Rect((0, 10, 10, 380))
border2 = pygame.Rect((590, 0, 10, 390))
screen = pygame.display.set_mode((screen_x, screen_y))
run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,255,255), boundary1)
    pygame.draw.rect(screen, (255, 255, 255), boundary2)
    pygame.draw.rect(screen, (255,0,0), border1)
    pygame.draw.rect(screen, (0, 255, 0), border2)
    pygame.draw.rect(screen, (255, 255, 255), player1)
    pygame.draw.rect(screen, (255, 255, 255), player2)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player1.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player1.move_ip(0, 1)
    if key[pygame.K_w]:
        player2.move_ip(0, -1)
    elif key[pygame.K_s]:
        player2.move_ip(0, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
