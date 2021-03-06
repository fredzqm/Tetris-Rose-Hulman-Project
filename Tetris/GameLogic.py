import pygame
import random
import GraphicsUtil as Graph
import Menu

import block_class
from block_class import Block

# import squareBlock
from squareBlock import squareBlock

# import lineBlock
from lineBlock import lineBlock

# import lBlock
from lBlock import lBlock

# import squiggleBlock
from squiggleBlock import squiggleBlock

# import Tblock
from Tblock import TBlock

#import squiggleBlock2
from squiggleBlock2 import squiggleBlock2

from lBlock2 import lBlock2



# pygame.mixer.music.play(-1)

#list of tetraminos
tetraminoList = [lBlock, lBlock2, squareBlock, lineBlock,
        squiggleBlock, squiggleBlock2, TBlock]

font = pygame.font.Font(None,36)
font2 = pygame.font.Font(None,14)

gameState= 'playing'
menuState = 'menu'
endGameState = 'game end'

state= menuState

tick = 10
permtick = tick
tickfast = tick * 10


BLACK = (0,0,0)
GREEN = (0, 255, 0)
x = 4
y = 0
ychange = 0
score = 0
level = 0

chazFundatory = pygame.image.load("fundatory.jpg")
chazFundatory = pygame.transform.scale(chazFundatory, (200,309))


def randomeBlock():
    global x, y
    x,y = 4, 0
    b = tetraminoList[random.randint(0, len(tetraminoList)-1)]
    return b()

currentblock = randomeBlock()
nextBlock = randomeBlock()

# currentblock = squareBlock()
    
#a method that checks collisions
def checkCollision():
    pts = currentblock.points()
    #print("checkCollision", x, y, pts)
    for p in pts:
        px, py = x+p[0], y+p[1]
        if px<0 or px>= len(Graph.TGrid[0]):
            return True
        if py<0 or py>= len(Graph.TGrid) -1 :
            return True
        if Graph.TGrid[py][px] != 0:
            return True
    return False

#a method that checks collisions
def land():
   # print("test")
    global currentblock, nextBlock
    pts = currentblock.points()
    for p in pts:
        px, py = x+p[0], y+p[1]
        Graph.TGrid[py][px] = currentblock.color
   # print(pts)
    currentblock = nextBlock
    nextBlock = randomeBlock()

def resetGame():
    global score, currentblock, nextBlock, level, tick, permtick, tickfast
    level = 0
    tick = 10
    permtick = tick
    tickfast = tick *10
    currentblock = nextBlock
    nextBlock = randomeBlock()
    score = 0
    Graph.TGrid = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
    


    

# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global currentblock, x,y, ychange, nextBlock, state, score
    if state == menuState:
        pass
    elif state == gameState:
        ychange += 1
        if ychange == 10:
            #print (1, checkCollision())
            y+=1
            #print (2, checkCollision())
            if checkCollision():
                y-=1
                #print (3, checkCollision())
                land()
            ychange = 0


# A method that keeps track of the block graphics
#def 


# A method that does all the drawing for you.
def draw(screen):
    #print(score)
    global currentblock, y, x, state, me
    if state == gameState: 
        # # setup a different background, 
        # if Graph.TGrid[y][x] != 0:
        #     y = 0
        #     x = 4
        #     currentblock = randomeBlock()
        screen.fill(Graph.BLACK)
        screen.blit(Graph.grid, (0, 0))
        

        def drawTetramino(x , y, block):
            pts = block.points()
            for p in pts:
                px, py = x+p[0], y+p[1]
                screen.blit(block.surface, (px*25+Graph.toplength, py*25+Graph.topwidth))
        
        drawTetramino(x, y, currentblock)

        for i in range (len(Graph.TGrid)):
            for j in range (len(Graph.TGrid[i])):
                loc = Graph.TGrid [i][j]
                if loc != 0:
                    if loc == 1:
                        b = Block(25,25, (255,0,0), j, i)
                        b.indBlock(screen,block_class.yellowBlock)
                    elif loc == 2:
                        b = Block(25,25, (255,0,0), j, i)
                        b.indBlock(screen,block_class.tealBlock)
                    elif loc == 3:
                        b = Block(25,25, (255,0,0), j, i)
                        b.indBlock(screen,block_class.redBlock)
                    elif loc == 4:
                        b = Block(25,25, (255,0,0), j, i)
                        b.indBlock(screen,block_class.greenBlock)
                    elif loc == 5:
                        b = Block(25,25, (255,0,0), j, i)
                        b.indBlock(screen,block_class.blueBlock)
                    elif loc == 6:
                        b = Block(25,25, (255,0,0), j, i)
                        b.indBlock(screen,block_class.orangeBlock)
                    elif loc == 7:
                        b = Block(25,25, (255,0,0), j, i)
                        b.indBlock(screen,block_class.purpleBlock)



        # Clear a row and score when complete
        bonus = -50
        for i in Graph.TGrid:
            global score, tick, permtick, level
            if 0 not in i:
                Graph.TGrid.remove(i)
                Graph.TGrid.insert(0,[0,0,0,0,0,0,0,0,0,0])
                score += 100
                level += 100
                bonus += 50
                if level >= 500:
                    level -= 500
                    permtick += 8
                    tick += 8
                
        if bonus >= 0:
            score += bonus
            level += bonus
            # return score
        text = font.render(str(score),1,(255,255,255))
   
        #Draws Boxes On The Side
        screen.blit(Graph.scoreSurface, (325, 400))
        
        screen.blit(Graph.scoreWordSurface, (325, 330))
        
        screen.blit(text, (335,415))

        screen.blit(Graph.nextSurface, (325, 50))

        screen.blit(Graph.nextShowSurface, (325, 115))

        drawTetramino(14.5, 6, nextBlock)
        
        screen.blit(Graph.gridGraphicSurface, (0, 0))  
        

        #Draws Box Behind Grid
        #screen.blit(Graph.gridGraphicSurface, (18, 5))  
    
    elif state == endGameState:
        

        # pygame.mixer.music.stop()

    
        
       # print ('endgame called')
        pygame.display.flip()

        endScoreSurface = pygame.Surface((200, 50))
        endScoreImage = pygame.image.load("ScoreBox.png")
        endScoreImage = pygame.transform.scale(endScoreImage, (200, 50))
        endScoreSurface.blit(endScoreImage, (0, 0))
        
        

        screen.fill(Graph.BLACK)
        text = font.render('Score: ' + str(score),1,(255,255,255))
        text2 = font.render('press M to return to menu',1,(255,255,255))
        screen.blit(endScoreSurface, (185,235))
        screen.blit(text, (205,250))
        screen.blit(text2, (130,450))
        


    elif state == menuState:       
        resetGame()
        pygame.display.flip()
        

       # print ('menu state called')
        screen.fill(Graph.BLACK)
        screen.blit(chazFundatory,(180,170))
        startbutton = Menu.Button("Play Game", screen, 180, 90, 200, 50)
        startbutton.draw(Menu.playButton)


