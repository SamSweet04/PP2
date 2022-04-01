import pygame
from datetime import datetime
import time

pygame.init()

WHITE = (255, 255, 255)
FPS = 1
theFont=pygame.font.Font(None,72)

screen = pygame.display.set_mode((700, 525))
clock = pygame.time.Clock()
image = pygame.image.load('mickey.png')
image_s = pygame.image.load('seconds.png')
image_m = pygame.image.load('minutes.png')

def blitRotate(surf, image, pos, angle):

    r_image = pygame.transform.rotate(image, angle)
    rect = image.get_rect(center = pos)

    rot_rect = r_image.get_rect(center = rect.center)
    surf.blit(r_image, rot_rect)

sec = datetime.now().strftime('%S')
min = datetime.now().strftime('%M')
angle_s = int(sec) * -6
angle_m = int(min) * -6
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    screen.blit(image,(0, 0))
    blitRotate(screen, image_s, (349.4, 261.75), angle_s)
    blitRotate(screen, image_m, (349.5, 262), angle_m)
    sec = datetime.now().strftime('%S')
    min = datetime.now().strftime('%M')
    angle_s = int(sec) * -6
    angle_m = int(min) * -6
    theTime=time.strftime("%H:%M:%S", time.localtime())
    timeText=theFont.render(str(theTime), True,(0,0,0),(255,0,0))
    screen.blit(timeText, (0,0))
    pygame.display.update()
pygame.quit()
