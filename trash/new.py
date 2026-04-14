import pygame


pygame.init()
screen = pygame.display.set_mode((400,300))
image = pygame.image.load('ball.png')
surface = pygame.Surface((100,100))
clock = pygame.time.Clock()
x,y = 30,30

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))

    screen.blit(image, (x,y))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    pygame.display.flip()
    clock.tick(60)