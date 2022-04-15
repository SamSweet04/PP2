#Imports
import random
import pygame
import math

#Create a function of main, where discribed the progress of work paint
def main():
    #Creating a black screen
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))
    #Creating a surface for intermediate rendering of figures
    work_surf = pygame.Surface((800, 600)) 
    #To define color of figure
    mode = 'random' 
    draw_on = False 
    #tuple of the initial coordinates of figure
    last_pos = (0, 0) 
    #The initial color
    color = (255, 128, 0) 
    #Length thickness
    radius = 1
    #To define what figure we picked
    figure = 'pen' 
    #Creating colors
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }
    #A function to define the coordinates, length and width of rectangle
    def Rect_pos(x1, y1, x2, y2): 
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)) 

    running = True

    #Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #Actions when you press the button
            if event.type == pygame.KEYDOWN:
                #To pick colors of figures
                if event.key == pygame.K_1: 
                    mode = 'red'
                if event.key == pygame.K_2: 
                    mode = 'blue'
                if event.key == pygame.K_3:
                    mode = 'green'
                #To pick what figure you want to draw
                if event.key == pygame.K_r: 
                    figure = 'rectangle'
                if event.key == pygame.K_p: 
                    figure = 'pen'
                if event.key == pygame.K_e: 
                    figure = 'erase'
                if event.key == pygame.K_c: 
                    figure = 'circle'
            #Event, which chooses random or different color of figure
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                draw_on = True 
                last_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP: 
                work_surf.blit(screen, (0, 0))
                draw_on = False
            #Event, which draws figure, depending on 'figure'
            if event.type == pygame.MOUSEMOTION: 
                if draw_on:
                    if figure == 'pen': 
                        pygame.draw.line(screen, color, last_pos, event.pos, radius)
                        last_pos = event.pos 
                    if figure == 'erase': 
                        pygame.draw.circle(screen, (0, 0, 0), (event.pos[0], event.pos[1]), 6)
                    if figure == 'rectangle': 
                        t = Rect_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(t))
                    if figure == 'circle': 
                        pygame.draw.circle(screen, color, (last_pos[0], last_pos[1]), int(math.sqrt((event.pos[0]-last_pos[0])**2 + (event.pos[1]-last_pos[1])**2)))

        pygame.display.flip() 

    pygame.quit() 

main() 
