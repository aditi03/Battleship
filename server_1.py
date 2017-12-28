import pygame
from pygame.locals import *
import sys
import socket
from thread import *
import threading

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

    font = pygame.font.Font(None, 20)
    rmsg='A'
    cmsg=1
    rx=215
    cy=165
    rx1=615

    for i in range(10):
        text = font.render(str(cmsg), 1, (10, 10, 10))
        background.blit(text, (180,cy))
        background.blit(text, (580,cy))
        text1 = font.render(str(rmsg), 1, (10, 10, 10))
        background.blit(text1, (rx,130))
        background.blit(text1, (rx1,130))
        cmsg=cmsg+1
        cy=cy+30
        rx=rx+30
        rx1=rx1+30
        rmsg=chr(ord(rmsg)+1)

    x=50
    for i in range(2):
        pygame.draw.rect(background,(128,128,128),(x,150,50,10))
        pygame.draw.rect(background,(128,128,128),(x,170,40,10))
        pygame.draw.rect(background,(128,128,128),(x,190,30,10))
        pygame.draw.rect(background,(128,128,128),(x,210,30,10))
        pygame.draw.rect(background,(128,128,128),(x,230,20,10))
        x=1000

    font = pygame.font.Font(None, 24)
    text = font.render('Your Grid', 1, (10, 10, 10))
    background.blit(text, (300,110))
    text = font.render('Opponent\'s Grid', 1, (10, 10, 10))
    background.blit(text, (680,110))


    return background

def position_ships(board):
    #Create Ready Button
    pygame.draw.rect(board,(0,0,0),(550,500,100,30),2)
    font = pygame.font.Font(None, 24)
    text = font.render('READY', 1, (10, 10, 10))
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

def threaded(c):
    while True:
 
        # data received from client
        data = c.recv(1024)
        print data
        if not data:
            print('Bye')
             
            # lock released on exit
            print_lock.release()
            break
 
        # reverse the given string from client
        data = raw_input('Enter msg:')
 
        # send back reversed string to client
        c.send(data)
 
    # connection closed
    c.close()


# initialize pygame and our window
pygame.init()
ttt = pygame.display.set_mode ((1100, 600))
pygame.display.set_caption ('BattleShip')

# create the game board
board = initBoard (ttt)
position_ships(board)
board=display_boards(ttt)

#c, addr = s.accept()     
#print 'Got connection from', addr

   # send a thank you message to the client. 
#c.send('Thank you for connecting')

# main event loop
#running = 1
crashed=False

#while (running == 1):
while not crashed:
    c, addr = s.accept()     
    print 'Got connection from', addr

   # send a thank you message to the client. 
    c.send('Thank you for connecting')
    for event in pygame.event.get():
        #if event.type is QUIT:
        if event.type==pygame.QUIT:
            crashed=True

            #running = 0
        print_lock.acquire()
        start_new_thread(threaded,(c,))
         # update the display
        showBoard (ttt, board)
        print_lock.release()
      
c.close()
pygame.quit()
quit()