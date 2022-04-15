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
    draw_on = False # Создаем переменную для отрисовки фигур
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
    #Creating an empty list of the points of triangles and rhombus
    points = list() 

    #A function to define the coordinates, length and width of rectangle
    def Rect_pos(x1, y1, x2, y2): 
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)) 

    #A function to define the coordinates and length of square
    def Square_pos(x1, y1, x2, y2): 
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2))

    #A function to define the coordinates of equilateral triangle
    def Equilateral_Triangle_pos(x1, y1, x2, y2): 
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x2+x2-x1, y1))
        return points

    #A function to define the coordinates of right triangle
    def Right_Triangle_pos(x1, y1, x2, y2): 
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x1, y2))
        return points

    #A function to define the coordinates of rhombus
    def Rhombus_pos(x1, y1, x2, y2): 
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x2-x1+x2, y1))
        points.append((x2, y1+y1-y2))
        return points

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
                if event.key == pygame.K_l: 
                    figure = 'erase'
                if event.key == pygame.K_c:
                    figure = 'circle'
                if event.key == pygame.K_s: 
                    figure = 'square'
                if event.key == pygame.K_e: 
                    figure = 'equilateral triangle'
                if event.key == pygame.K_t: 
                    figure = 'right triangle'
                if event.key == pygame.K_a:
                    figure = 'rhombus'
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
                    #Depending on value of 'figure', we draw figure with color that we chose before
                    if figure == 'pen': 
                        pygame.draw.line(screen, color, last_pos, event.pos, radius)
                        last_pos = event.pos 
                    if figure == 'erase': 
                        pygame.draw.circle(screen, (0, 0, 0), (event.pos[0], event.pos[1]), 6)
                    if figure == 'rectangle':
                        t = Rect_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(t))
                    if figure == 'square':
                        t = Square_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(t))
                    if figure == 'equilateral triangle': 
                        t = Equilateral_Triangle_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = [] 
                    if figure == 'right triangle': 
                        t = Right_Triangle_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = [] 
                    if figure == 'rhombus':
                        t = Rhombus_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = []
                    if figure == 'circle':  
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.circle(screen, color, (last_pos[0], last_pos[1]), int(math.sqrt((event.pos[0]-last_pos[0])**2 + (event.pos[1]-last_pos[1])**2)))

        pygame.display.flip() 

    pygame.quit() 

main() 
