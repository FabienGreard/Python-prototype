
import os
import pygame
from pygame.locals import *

#initialize pygame
pygame.init()

#windows frame
windows = pygame.display.set_mode((640,480), RESIZABLE)

#background
background = pygame.image.load("background.jpg").convert()
windows.blit(background, (0,0))

#character
character = pygame.image.load("perso.png").convert_alpha()
#pos_character = character.get_rect()
#windows.blit(character, pos_character)
chara_x = 0
chara_y = 0
windows.blit(character, (chara_x, chara_y))

#reloading
pygame.display.flip()

#allow the keep pushing button
pygame.key.set_repeat(400, 30)

#keep the frame open
while True:
    for event in pygame.event.get():

        #check if keydown
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                pos_character = pos_character.move(0,3)

        #follow the mousse 
        if event.type == MOUSEMOTION:
            chara_x = event.pos[0]
            chara_y = event.pos[1]

        #check alt + F4 or close the program
        if event.type == QUIT:
            os.sys.exit(0)
            break

        windows.blit(background, (0,0))
        #windows.blit(character, pos_character)
        windows.blit(character, (chara_x, chara_y))
        pygame.display.flip()