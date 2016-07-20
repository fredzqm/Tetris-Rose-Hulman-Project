import pygame
from pygame import *
import block_class
from block_class import Block

blockWidth = 25
x = 0
y = 0

squiggleSurface = pygame.Surface((75,50))
squiggleSurface.set_colorkey((0,0,0))


B1 = Block(blockWidth,blockWidth, (0,255,255), x, y)
B2 = Block(blockWidth,blockWidth, (0,255,255), x+1, y)
B3 = Block(blockWidth,blockWidth, (0,255,255), x+1, y+1)
B4 = Block(blockWidth,blockWidth, (0,255,255), x+2, y+1)

B1.groupDrawSquiggleBlock(squiggleSurface)
B2.groupDrawSquiggleBlock(squiggleSurface)
B3.groupDrawSquiggleBlock(squiggleSurface)
B4.groupDrawSquiggleBlock(squiggleSurface)

class squiggleBlock:
    def __init__(self):
        self.surface = squiggleSurface
    
    def draw(self, screen, x,y):
        screen.blit(self.surface, (x*25, y*25))

class squiggleBlock2:
    def __init__(self):
       self.surface = squiggleSurface
    
    def draw(self, screen,x,y):
        screen.blit(pygame.transform.flip(self.surface, True, False), (x*25, y*25))

# while True:
#     if __name__ == "__main__":
#         pygame.init()
#         screen = pygame.display.set_mode((500, 500))
#         b = squiggleBlock2(200,200)
#         screen.fill((255, 255,255))
#         b.draw(screen)

#         # screen.blit(b, (200, 200))
#         eventList = pygame.event.get()
#         for event in eventList:
#             if event.type == pygame.QUIT:
#                     # if someone tries to close the Windows
#                     exit()

#         pygame.display.flip()        
       
