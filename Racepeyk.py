import pygame
import time
import random
pygame.init()

crash_sound = pygame.mixer.Sound("moto10000.wav")
pygame.mixer.music.load("moto20.wav")

display_width = 1200
display_height = 680
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('RacePeyk')

clock = pygame.time.Clock()

carImg = pygame.image.load('motor.png')
carImg = pygame.transform.scale(carImg, (100, 100))
car_height = 95
backpicroad = pygame.image.load('road.png')
backpicsky = pygame.image.load('sky.png')
backpicteh = pygame.image.load('back_teh3.png')
intro_pic = pygame.image.load('intro1.jpg')
thing=[0,1,2,3,4,5]
for i in range(5):
    thing[i] = pygame.image.load('1_%d.png'%i)
thingwidth = [206,264,249,218,230,210]
thingheight= [71,80,76,73,74,76]
def buttom(msg,x,y,w,h,ic,ac,action=None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    
    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "Play" :
                game_loop()
            elif action == "Quit":
                pygame.quit()
                quit()
            
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",25)
    TextSurf , TextRect = text_objects(msg,smallText)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf,TextRect)
    
def game_intro():
    intro = True
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(intro_pic,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf , TextRect = text_objects("",largeText)
        TextRect.center = ((display_width/2) ,(display_height/2 ))
        gameDisplay.blit(TextSurf , TextRect )

        buttom("Play !",200,450,150,75,(0,200,0),(0,250,0),"Play")
        buttom("Quit ",800,450,150,75,(200,0,0),(255,0,0),"Quit")
        
        pygame.display.update()
        

def score(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("score : "+ str(count),True ,(155,0,0))
    gameDisplay.blit(text,(0,0))


def stuff(stuffx,stuffy,picNO):
    gameDisplay.blit(thing[picNO],(stuffx,stuffy))
    
def car (x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,(0,0,0))
    return textSurface , textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf , TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2) ,(display_height/2 ))
    gameDisplay.blit(TextSurf , TextRect )
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf , TextRect = text_objects("YOU CRASHED !",largeText)
    TextRect.center = ((display_width/2) ,(display_height/2 ))
    gameDisplay.blit(TextSurf , TextRect )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        buttom("Try again !",200,500,150,75,(0,200,0),(0,250,0),"Play")
        buttom("Quit ",800,500,150,75,(200,0,0),(255,0,0),"Quit")
        

        pygame.display.update()
    
    
def game_loop():
    pygame.mixer.music.play(-1)

    x = 50
    y = 400

    y_change = 0

    stuff_startx = 1600
    stuff_starty = random.randrange(420,display_height-120,43)
    stuff_speed = -7
    picNO=random.randrange(0,5)#
    counter = 0
    deltax = 0
    deltax1 = 0

    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        y += y_change

        gameDisplay.blit(backpicroad, (2400 - deltax, 470))
        gameDisplay.blit(backpicroad, (-deltax, 470))
        gameDisplay.blit(backpicsky, (2400 - deltax, 0))
        gameDisplay.blit(backpicsky, (-deltax, 0))
        gameDisplay.blit(backpicteh, (2400 -deltax1/30, 55))
        gameDisplay.blit(backpicteh, ( -deltax1/30, 55))
        if y<=stuff_starty:
            car(x,y)
            stuff(stuff_startx,stuff_starty,picNO)
            stuff_startx += stuff_speed
        if y>stuff_starty:
            stuff(stuff_startx,stuff_starty,picNO)
            stuff_startx += stuff_speed
            car(x,y)
            
        score(counter)
        if y > display_height - car_height or y < 380:
            crash()
        deltax = (deltax + 20) % 2400
        deltax1 = (deltax1 + 20) % 72000

        if stuff_startx < -500:
            stuff_startx = 1200
            stuff_starty=random.randrange(420,510,30)
            picNO = random.randrange(0,5)
            thingN= thing[picNO]
            counter += 1
            if (counter % 5 == 0 ):
                stuff_speed += -4

        if x + car_height > stuff_startx and x + car_height < stuff_startx + thingwidth[picNO]:
            if y > stuff_starty and y <= stuff_starty + thingheight[picNO] or y + car_height > stuff_starty and y + car_height < stuff_starty + thingheight[picNO] or y < stuff_starty and y + car_height > stuff_starty + thingheight[picNO] or (y+car_height/2)>stuff_starty and (y+car_height/2)<stuff_starty+thingheight[picNO]:
                crash()
                
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
