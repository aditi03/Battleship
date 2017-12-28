import pygame
from pygame.locals import *

# declare our global variables for the game

Mygrid = [ [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ] ]

Enemygrid = [ [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ], \
         [ None, None, None, None, None, None, None, None, None,None ] ]


#declare our support functions

def initBoard(b):
    background=pygame.Surface(b.get_size())
    background=background.convert()
    background.fill((250,250,250))

    #vertical lines
    #pygame.draw.line (background, (0,0,250), (200, 150), (200, 450), 2)
    x=200
    y=150
    for i in range(11):
        pygame.draw.line (background, (0,0,250), (x, 150), (x, 450), 2)
         # horizontal lines
        pygame.draw.line (background, (0,0,250), (200, y), (500, y), 2)
        x=x+30
        y=y+30
    #pygame.draw.line (background, (0,0,250), (500, 150), (500, 450), 2)

    # horizontal lines
    #pygame.draw.line (background, (0,0,250), (200, 150), (500, 150), 2)
    #pygame.draw.line (background, (0,0,250), (200, 450), (500, 450), 2)
    return background

def showBoard (ttt, board):
    # redraw the game board on the display
    # ---------------------------------------------------------------
    # ttt   : the initialized pyGame display
    # board : the game board surface

    
    ttt.blit (board, (0, 0))
    pygame.display.flip()

# initialize pygame and our window
pygame.init()
ttt = pygame.display.set_mode ((1100, 600))
pygame.display.set_caption ('BattleShip')

# create the game board
board = initBoard (ttt)

# main event loop
#running = 1
crashed=False

#while (running == 1):
while not crashed:
    for event in pygame.event.get():
        #if event.type is QUIT:
        if event.type==pygame.QUIT:
            crashed=True
            #running = 0
      
         # update the display
        showBoard (ttt, board)
      
pygame.quit()
quit()


    


