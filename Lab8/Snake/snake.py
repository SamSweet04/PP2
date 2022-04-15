#Imports
import pygame
from random import randrange
import random
import time

#Initialzing
pygame.init()

#Setting up FPS
FPS = 3
clock = pygame.time.Clock()

#Creating colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Other Variables for use in the program
WIDTH, HEIGHT = 500, 500
BLOCK_SIZE= 20
level = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 20, False)
font1 = pygame.font.SysFont("Verdana", 30, False)

#Crearing a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

running = True

class Food:
    def __init__(self):
        self.x = randrange(0, WIDTH, BLOCK_SIZE)
        self.y = randrange(0, HEIGHT, BLOCK_SIZE)
   
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)) 
    
    def redraw(self):
        self.x = randrange(0, WIDTH, BLOCK_SIZE)
        self.y = randrange(0, HEIGHT, BLOCK_SIZE)
    

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

class Snake:
    def __init__(self):
        self.speed = BLOCK_SIZE
        self.score = 0
        self.body = [[40, 40],[500, 500],[520, 520]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = BLUE
    
    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.destination != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_d and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_w and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_s and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        #Collosion occurs between snake and borders
        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT

    def draw(self):
        for block in self.body:
            pygame.draw.circle(screen, self.color, (block[0] + 10, block[1] + 10), BLOCK_SIZE/2)

    #A function to check if snake and food cross
    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.score += random.randint(1, 3)
            self.body.append([500, 500])
    #A function to check if snake's head and body cross
    def collide_self(self):
        global running
        if self.body[0] in self.body[1:]:
            running = False
    #Checking if food will appear in the snake's body
    def check_food(self, f:Food):
        if [f.x, f.y] in self.body:
            f.redraw()

#Setting up Classes
s = Snake()
f = Food()

#Game Loop
while running:
    clock.tick(FPS)
    events = pygame.event.get()
    #Cycles through all events occurring  
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    #White screen
    screen.fill(WHITE)
    #Change of levels and speed
    if s.score >= 3:
        level = 1
        FPS = 5
    if s.score >= 6:
        level = 2
        FPS = 5
    if s.score >= 9:
        level = 3
        FPS = 6
    if s.score >= 12:
        level = 4
        FPS = 7
    if s.score >= 15:
        level = 5
        FPS = 7
    #Actions to get structure of walls
    walls_coor=  open(f'level{level}.txt', 'r').readlines()
    
    walls = []

    for i, line in enumerate(walls_coor):
        for j, each in enumerate(line):
            if each == "#":
                walls.append(Wall(j * BLOCK_SIZE, i * BLOCK_SIZE))
    for wall in walls:
        wall.draw()
        #Checking if food will appear in the walls
        if f.x == wall.x and f.y == wall.y:
            f.redraw()
         #Checking if snake and wall cross
        if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
             screen.fill(RED)
             screen.blit(score, (150, 200))
             pygame.display.update()
             time.sleep(3)
             running = False
    #Moves, re-draws and other functions with snake, food
    f.draw()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.collide_self()
    s.check_food(f)

    #Setting up Fonts 
    score = font1.render(f'Your score: {s.score}', True, BLACK)
    text = font.render(f"Score: {s.score}", True, BLACK)
    text2 = font.render(f"Level: {level}", True, BLACK)
    screen.blit(text, (5, 0))
    screen.blit(text2, (5, 30))
    pygame.display.flip()
pygame.quit()
