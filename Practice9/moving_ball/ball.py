import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 25
        self.color = (255,0,0)
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_power = -20

    def jump(self):
        if self.y >= 575:
            self.velocity_y = self.jump_power

    def update(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        if self.y >= 575:
            self.y = 575
            self.velocity_y = 0

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.jump()
        if pressed[pygame.K_LEFT]:
            if self.x - self.radius > 0:
                self.x -= 10
        if pressed[pygame.K_RIGHT]:
            if self.x + self.radius < 800:
                self.x += 10

    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)