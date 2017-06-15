
import os
import pygame
from pygame.locals import *

#initialize pygame
pygame.init()

#windows frame
windows = pygame.display.set_mode((640,480), RESIZABLE)

#keep the frame open
while True:
    key = input()
    if key == 'q':
        os.sys.exit(0)
        break
