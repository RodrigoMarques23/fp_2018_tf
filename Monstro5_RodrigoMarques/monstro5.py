
import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 1000
WINDOWHEIGHT = 530
TEXTCOLOR = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BACKGROUNDCOLOR = (255,0,0)
BLACK = (0,0,0)
FPS = 60
PLAYERMOVERATE = 5



def terminate():
    pygame.quit()
    sys.exit()

def PlayerHasHitPoco():
    return 0

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: #_______________________________________________________ Pressing ESC quits._______________________________________________________
                    terminate()
                return

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# _______________________________________________________Set up pygame, the window, and the mouse cursor._______________________________________________________
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Set up the fonts.
font = pygame.font.SysFont(None, 48)

# ______________________________________________________________________________Set up images______________________________________________________________
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()

background_image = pygame.image.load('map.png').convert()
transparent_image = pygame.image.load('map.png').convert()
ouro_image = pygame.image.load('ouro.png').convert()
partida_image = pygame.image.load('ppartida.png').convert()
monstro_image = pygame.image.load('monstro.png').convert()

#______________________________ _______________________________________________________Show the "Start" screen._______________________________________________________
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Monstro', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press any key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # _______________________________________________________Set up the start of the game._______________________________________________________
    UP = True
    player = []
    gold = False
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False

    while True: # _______________________________________________________GameLoop_______________________________________________________
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False
                
                    

            

        # _______________________________________________________Move the player around._______________________________________________________
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            if UP == True:
                playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        #blocks_____________________________________
            #rect1

        #if moveLeft and playerRect.left < TPC.right and playerRect > TPC.bottom:
            moveRight = False
            moveLeft = False

        #if playerHasHitTPC(playerRect, TPC):
          #  pygame.quit()
        #_______________________________________________________ Draw the game world on the window._______________________________________________________
        


        # Draw the player's rectangle.
        #windowSurface.blit(playerImage, playerRect)

        TPC = pygame.draw.rect(windowSurface, GREEN ,[0,245,470,50])
        agua = pygame.draw.rect(windowSurface, GREEN, [0,245,177,300])
        agua1 = pygame.draw.rect(windowSurface, GREEN, [823,245,177,300])
        agua2 = pygame.draw.rect(windowSurface, GREEN, [535,245,470,50])
        agua3 = pygame.draw.rect(windowSurface, GREEN, [290,180,180,70])
        agua4 = pygame.draw.rect(windowSurface, GREEN, [290,120,180,70])
        agua5 = pygame.draw.rect(windowSurface, GREEN, [0,180,400,70])
        
        
        windowSurface.blit(background_image, [0,0])
        windowSurface.blit(playerImage, playerRect)
        ouro = windowSurface.blit(ouro_image, [950,100])
        ponto = windowSurface.blit(partida_image,[450,500])

        #monstros
        monstro1 = windowSurface.blit(monstro_image, [470,50])
        monstro2 = windowSurface.blit(monstro_image, [510,380])
        
        #lasers.tesouro
        corda1 = pygame.draw.rect(windowSurface, RED, [930,80,80,3])
        corda2 = pygame.draw.rect(windowSurface, RED, [880,110,3,50])

        #lasers.ponte
        Lclaymore1 = pygame.draw.rect(windowSurface, RED, [510,180,15,2])
        Lclaymore2 = pygame.draw.rect(windowSurface, RED, [510,185,15,2])
        Lclaymore3 = pygame.draw.rect(windowSurface, RED, [510,190,15,2])

        
        pygame.display.update()

        if playerRect.colliderect(ponto):
            if gold == False:
                drawText('Ainda não tens o ouro...', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                pygame.display.update()
            else:
                drawText('Parabéns! Ganhaste!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
                break
        if playerRect.colliderect(ouro):
            gold = True
            drawText('Já tens o ouro! Volta para a casa partida!!', font, windowSurface, (WINDOWWIDTH / 3)-200, (WINDOWHEIGHT / 3))
            pygame.display.update()
        if playerRect.colliderect(TPC):
            drawText('Ups... caíste na lava!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        #colisaoMonstro
        if playerRect.colliderect(monstro1):
            drawText('Não te deixes apanhar pelo monstro... Comeu-te vivo.', font, windowSurface, (WINDOWWIDTH / 3-200), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(monstro2):
            drawText('Não te deixes apanhar pelo monstro... Comeu-te vivo.', font, windowSurface, (WINDOWWIDTH / 3-200), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        
        #colisaoAgua
        if playerRect.colliderect(agua):
            drawText('Ups... caíste na lava!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(agua1):
            drawText('Ups... caíste na lava!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(agua2):
            drawText('Ups... caíste na lava!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(agua3):
            drawText('Ups... caíste na lava!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(agua4):
            drawText('Ups... caíste na lava!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(agua5):
            drawText('Ups... caíste na lava!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        #colisaoLasers.ponte
        if playerRect.colliderect(Lclaymore1):
            drawText('Cuidado com os lasers... ficaste feito em bocados.', font, windowSurface, (WINDOWWIDTH / 3-170), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(Lclaymore2):
            drawText('Cuidado com os lasers... ficaste feito em bocados.', font, windowSurface, (WINDOWWIDTH / 3-170), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(Lclaymore3):
            drawText('Cuidado com os lasers... ficaste feito em bocados.', font, windowSurface, (WINDOWWIDTH / 3-170), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        #colisaoLasers.ouro
        if playerRect.colliderect(corda1):
            drawText('Cuidado com os lasers... ficaste feito em bocados', font, windowSurface, (WINDOWWIDTH / 3-170), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break
        if playerRect.colliderect(corda2):
            drawText('Cuidado com os lasers... ficaste feito em bocados', font, windowSurface, (WINDOWWIDTH / 3-170), (WINDOWHEIGHT / 3))
            pygame.display.update()
            break




        mainClock.tick(FPS)

    drawText('Carrega em qualquer tecla para voltares a jogar', font, windowSurface, (WINDOWWIDTH / 3)-150 , (WINDOWHEIGHT / 3) + 40)
    pygame.display.update()
    waitForPlayerToPressKey()
