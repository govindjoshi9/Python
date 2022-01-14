import random
import sys
import pygame
from pygame.locals import*

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENHEIGHT,SCREENWIDTH))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'C:/Users/sundaram infotech/Documents/Python/Project2/sprites/bird.png'
BACKGROUND = 'C:/Users/sundaram infotech/Documents/Python/Project2/sprites/background.png'
PIPE = 'C:/Users/sundaram infotech/Documents/Python/Project2/sprites/pipe.png'

def welcomeScreen():
    """
    Shows welcome images on the screen
    """
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)

                

if __name__ == '__main__':
    #This will be the main function our game will start

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/0.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/1.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/2.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/3.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/4.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/5.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/6.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/7.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/8.png').convert_alpha(),
        pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/8.png').convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/message.png').convert_alpha(),
    GAME_SPRITES['base'] = pygame.image.load('C:/Users/sundaram infotech/Documents/Python/Project2/sprites/base.png').convert_alpha(),
    GAME_SPRITES['pip'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
     pygame.image.load(PIPE).convert_alpha(),
    )


    GAME_SOUNDS['die'] = pygame.mixer.Sound('C:/Users/sundaram infotech/Documents/Python/Project2/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('C:/Users/sundaram infotech/Documents/Python/Project2/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('C:/Users/sundaram infotech/Documents/Python/Project2/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('C:/Users/sundaram infotech/Documents/Python/Project2/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('C:/Users/sundaram infotech/Documents/Python/Project2/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()


    while True:
        welcomeScreen()
        # mainGame()