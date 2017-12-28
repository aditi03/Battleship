import pygame
from pygame.locals import *
import sys
import socket
from thread import *
import threading

# declare our global variables for the game
stage=0
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

s = socket.socket()         
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port=12345              

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))        
print "socket binded to %s" %(port)

# put the socket into listening mode
s.listen(5)     
print "socket is listening"
print_lock = threading.Lock()         
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
    #pygame.draw.rect(background,(0,0,250),(600,200,90,30))
    #pygame.display.flip()
    return background

def showBoard (ttt, board):
    # redraw the game board on the display
    # ---------------------------------------------------------------
    # ttt   : the initialized pyGame display
    # board : the game board surface

    
    ttt.blit (board, (0, 0))
    pygame.display.flip()

def display_boards(b):
    background=pygame.Surface(b.get_size())
    background=background.convert()
    background.fill((250,250,250))

    #vertical lines
    #pygame.draw.line (background, (0,0,250), (200, 150), (200, 450), 2)
    x=200
    x1=600
    y=150
    y1=150
    font = pygame.font.Font(None, 20)
    rmsg='A'
    cmsg=1
    rx=195
    cy=165

    for i in range(11):
        pygame.draw.line (background, (0,0,250), (x, 150), (x, 450), 2)
        pygame.draw.line (background, (0,0,250), (x1, 150), (x1, 450), 2)
         # horizontal lines
        pygame.draw.line (background, (0,0,250), (200, y), (500, y), 2)
        pygame.draw.line (background, (0,0,250), (600, y1), (900, y1), 2)
        x=x+30
        x1=x1+30
        y=y+30
        y1=y1+30
        text = font.render(str(cmsg), 1, (10, 10, 10))
        board.blit(text, (195,cy))
        cmsg=cmsg+1
        cy=cy+30

    return background

def position_ships(board):
    #Create Ready Button
    pygame.draw.rect(board,(0,0,0),(550,500,100,30),2)
    font = pygame.font.Font(None, 24)
    text = font.render('READY', 1, (10, 10, 10))
    #board.fill ((250, 250, 250), (0, 300, 300, 25))
    board.blit(text, (570,510))

    #Ready Button Clicked

    crashed=False

#while (running == 1):
    while not crashed:
        for event in pygame.event.get():
        #if event.type is QUIT:
            if event.type==pygame.QUIT:
                crashed=True
            #running = 0
            if event.type==pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print str(mouseX)+' '+str(mouseY)
                if 550<=mouseX<=650 and 500<=mouseY<=600:
                    return
         # update the display
        showBoard (ttt, board)


# initialize pygame and our window
pygame.init()
ttt = pygame.display.set_mode ((1100, 600))
pygame.display.set_caption ('BattleShip')

# create the game board
board = initBoard (ttt)
position_ships(board)
board=display_boards(ttt)

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