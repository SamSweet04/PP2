import pygame
pygame.init()

WIDTH, HEIGHT = 400, 800
FPS = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music')

clock = pygame.time.Clock()

playlist = list()
playlist.append ( "konfuz.mp3" )
playlist.append ( "Ariana Grande feat Ty ... - safety net.mp3" )
playlist.append ( "Nessa Barett feat jxdn - la di die.mp3" )
playlist.append ( "By Индия - думать о тебе.mp3" )
playlist.append ( "Скриптонит - Мистер 718.mp3" )
playlist.append ( "Billie Eilish  Khalid - lovely.mp3" )
playlist.append ( "Selena Gomez feat Gucc... - Fetish.mp3" )
playlist.append ( "Shawn Mendes  Justin B... - Monster.mp3" )
playlist.append ( "Shawn Mendes feat Khalid - Youth.mp3" )
playlist.append ( "Billie Eilish - bad guy.mp3" )

pygame.mixer.music.load(playlist.pop()) 
pygame.mixer.music.set_endevent(pygame.USEREVENT)    
pygame.mixer.music.play() 

image=list()
image.append("konfuz.jpg")
image.append("ariana.jpg")
image.append("la da die.jpg")
image.append("думать о тебе.jpg")
image.append("Мистер 718.jpg")
image.append("lovely.jpg")
image.append("fetish.jpg")
image.append("monster.jpg")
image.append("youth.jpg")
image.append("bad guy.jpg")

          
img = pygame.image.load(image.pop())

def nextsong():
    global playlist
    playlist = playlist[1:] + [playlist[0]]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

def prevsong():
    global playlist
    playlist = [playlist[-1]] + playlist[:-1]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

finished = False
while not finished:
    clock.tick(FPS)

    music_number=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finished=True
            if finished == True:
                pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pygame.mixer.music.stop()
                nextsong()
                image = image[1:] + [image[0]]
                img=pygame.image.load(image[0])
            if event.key==pygame.K_RIGHT:
                pygame.mixer.music.stop()
                prevsong()
                image = [image[-1]] + image[:-1]
                img=pygame.image.load(image[0])
            if event.key==pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key==pygame.K_s:
                pygame.mixer.music.unpause()
            if event.key==pygame.K_1:
                pygame.mixer.music.set_volume(0.3)
            if event.key==pygame.K_2:
                pygame.mixer.music.set_volume(1)

        if event.type == pygame.USEREVENT:    
            if len(playlist)>0:       
                pygame.mixer.music.queue(playlist.pop())
    
    screen.blit(pygame.transform.scale(img, (400, 800)), (0, 0))
    pygame.display.flip()
pygame.quit()
