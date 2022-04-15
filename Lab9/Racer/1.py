#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
PURPLEBLUE = (204, 204, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_PICKED = False
COIN_SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


background = pygame.image.load("./images/AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
# класс Врага
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
      #создаем метод,задаем скорость,создаем обьект заново с условием
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# класс Игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
# класс Монеты
class Coin(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("images\Coin.png")
            self.surf = pygame.Surface((25, 25))
            self.rect = self.surf.get_rect(center = (random.randint(150, 400), 0))

        def move(self):
                    global COIN_PICKED
                    self.rect.move_ip(0, 4)
                    if (self.rect.bottom > 600):
                        self.rect.top = 0
                        self.rect.center = (random.randint(150, 400), 0)
                    elif COIN_PICKED:
                        self.rect.top = 0
                        self.rect.center = (random.randint(150, 400), 0)
                        COIN_PICKED = False          
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

all_sprites.add(C)
coins = pygame.sprite.Group()
coins.add(C)
player = pygame.sprite.Group()
player.add(P1)

       
#Game Loop
while True:
      
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # блитим очки
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    # блитим кол.собранных монет с разными значениями
    cash_txt = font_small.render(str(COIN_SCORE), True, RED)
    DISPLAYSURF.blit(cash_txt, (380, 15))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # подбор монет
    for coin in coins:
        for pl in player:
            if pygame.sprite.collide_rect(pl, coin):
                COIN_SCORE += random.randint(1,3)
                COIN_PICKED = True
                pygame.mixer.Sound('sounds\coin.wav').play()
                coin.remove()
    # когда кол.монет достигает или превышает 10,скорость становиться равен 7
    if COIN_SCORE >= 10:
        SPEED = 7

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('./sounds/crash.wav').play()
          time.sleep(0.5)
          # если гэйм овер тогда выводим красное окно и кол.собранных монет
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          scores = font_small.render(f'Your score is: {COIN_SCORE}',True,BLACK)
          DISPLAYSURF.blit(scores, (120,330))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()    
    pygame.display.update()
    FramePerSec.tick(FPS)