import pygame
from pygame import *
import block_class
from block_class import Block
from GraphicsUtil import toplength, topwidth

blockWidth = 25
lineXpos = 0
lineYpos = 0

BLUE = (0,0,255)

lineSurface = Surface((25,100))
lineSurface.set_colorkey((0,0,0))

B1 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos)

B1.groupDrawLineBlock(lineSurface)


class lineBlock:
    def __init__(self):
        self.color = 2
        self.surface = lineSurface
        self.rotate = 0

    def points(self):
        if self.rotate%2==0:
            return [(0,0), (0,1), (0,2), (0,3)]
        if self.rotate%2==1:
            return [(0,0), (1,0), (2,0), (3,0)]
    
# while True:
#     if __name__ == "__main__":
#         pygame.init()
#         screen = pygame.display.set_mode((500, 500))
#         b = lineBlock(200,200)
#         screen.fill((255, 255,255))
#         b.draw(screen)

#         # screen.blit(b, (200, 200))
#         eventList = pygame.event.get()
#         for event in eventList:
#             if event.type == pygame.QUIT:
#                     # if someone tries to close the Windows
#                     exit()

#         pygame.display.flip()
    

       
 