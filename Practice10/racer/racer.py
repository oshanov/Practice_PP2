import pygame, random, time
from pygame.locals import *

BLACK = (0,0,0) #Initializing some constants
WHITE = (255,255,255)
GREY = (128,128,128)
RED = (255,0,0)

pygame.init() #Initializing pygame; screen`s size, background, name.
screen = pygame.display.set_mode((400,600))
screen.fill(WHITE)
background = pygame.image.load('AnimatedStreet.png')
FPS = pygame.time.Clock()
pygame.display.set_caption('Game')
coin_pickup = pygame.mixer.Sound('ding.mp3')

done = False
SPEED = 5
SCORE = 0
COINS = 0

font = pygame.font.SysFont('Verdana', 60)
sfont = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game Over', True, BLACK)

class Enemy(pygame.sprite.Sprite): #Creating enemy class, his image, movements
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)

        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)

    def draw(self,surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.image = pygame.transform.scale(self.image, (70,70))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,360),0)

    def move(self):
        self.rect.move_ip(0,2)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0) 
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def pickup(self):
        self.rect.y = -50

class Player(pygame.sprite.Sprite): #Same with player
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.move_ip(-SPEED,0)
        if pressed[pygame.K_RIGHT]:
            if self.rect.right < 400:
                self.rect.move_ip(SPEED,0)
        # if pressed[pygame.K_UP]:
        #     if self.rect.top > 0:
        #         self.rect.move_ip(0,-5)
        # if pressed[pygame.K_DOWN]:
        #     if self.rect.bottom < 600:
        #         self.rect.move_ip(0,5)

    def draw(self,surface):
        surface.blit(self.image, self.rect)

    

P1 = Player() #Initializing objects(sprites) andd adding them into corresponding groups
E1 = Enemy()
coin = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
bonus = pygame.sprite.Group()
bonus.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(coin)

INC_SPEED = pygame.USEREVENT + 1 #Creating new event
pygame.time.set_timer(INC_SPEED, 1000)

while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            if SPEED < 15:
                SPEED += 0.5

        if event.type == pygame.QUIT:
            pygame.quit()
            done = True

    screen.blit(background,(0,0) )
    scores = sfont.render(f'{SCORE}', True, BLACK)
    conins = sfont.render(f'{COINS}', True, BLACK)
    screen.blit(scores, (10,10))
    screen.blit(conins, (375,10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
            
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30,250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        
        time.sleep(2)
        pygame.quit()
        done = True

    if pygame.sprite.spritecollideany(P1, bonus):
        COINS += 1
        coin_pickup.play()
        coin.pickup()

    pygame.display.update()
    FPS.tick(60)
