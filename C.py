import pygame
from pygame.locals import *
import sys
import socket
from thread import *
import threading
import time
import math

# declare our global variables for the game
myGrid = [ [ None, None, None, None, None, None, None, None, None,None ], \
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
count=0
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

drag=0
img_pos=[]
marked=[]
ornt=list()
prev_x=0
prev_y=0
#declare our support functions

def initBoard(b):
    background=pygame.Surface(b.get_size())
    background=background.convert()
    background.fill((250,250,250))


    ships=['Carrier','Battleship','Cruiser','Submarine','Destroyer']
    pos=[[700,180],[730,240],[760,300],[760,360],[790,420]]
  
    #image load
    ''' for s in ships:
    
        image = pygame.image.load("C:\\Python27\\HandsOn\\BattleShip\\"+s+".png").convert()
        background.blit(image, (pos[a][0],pos[a][1]))
        
        a=a+1'''

            
    
    #pygame.display.update()
    #surf=pygame.transform.rotate(image_surf,90)
    #background.blit(surf, (700, 180))
    
    color=(25,100,150)
    '''pygame.draw.rect(background,color,(700,180,150,30))
    font = pygame.font.Font(None, 24)
    text = font.render('CARRIER', 1, (255, 255, 255))
    background.blit(text, (740,186))'''
    
    
    '''pygame.draw.rect(background,color,(700,240,120,30))
    font = pygame.font.Font(None, 24)
    text = font.render('BATTLESHIP', 1, (255, 255, 255))
    background.blit(text, (710,246))
    
    pygame.draw.rect(background,color,(700,300,90,30))
    font = pygame.font.Font(None, 24)
    text = font.render('CRUISER', 1, (255, 255, 255))
    background.blit(text, (710,306))
    
    pygame.draw.rect(background,color,(700,360,90,30))
    font = pygame.font.Font(None, 21)
    text = font.render('SUBMARINE', 1, (255, 255, 255))
    background.blit(text, (701,366))
    
    pygame.draw.rect(background,color,(700,420,60,30))
    
    font = pygame.font.Font(None, 13)
    text = font.render('DESTROYER', 1, (255, 255, 255))
    background.blit(text, (703,427))
    #pygame.display.update()'''

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
    pygame.draw.line (background, (0,0,250), (200, 150), (200, 450), 2)
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
    a=0
    ships=['Carrier','Battleship','Cruiser','Submarine','Destroyer']
    for s in ships:
        if ornt[a]=='v':
            image = pygame.image.load("C:\\Python27\\HandsOn\\BattleShip\\"+s+"_R.png").convert()
            background.blit(image, (img_pos[a][0],img_pos[a][1]))
        else:
            image = pygame.image.load("C:\\Python27\\HandsOn\\BattleShip\\"+s+".png").convert()
            background.blit(image, (img_pos[a][0],img_pos[a][1]))
            
        a=a+1
        showBoard(ttt,background)
        
    
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


def position(board):
    ships=['Carrier','Battleship','Cruiser','Submarine','Destroyer']
    pos=[[700,180],[730,240],[760,300],[760,360],[790,420]]
    a=0

    
    font = pygame.font.Font(None, 20)
    rmsg='A'
    cmsg=1
    rx=215
    cy=165
    rx1=615

    for i in range(10):
        text = font.render(str(cmsg), 1, (10, 10, 10))
        board.blit(text, (180,cy))
       
        text1 = font.render(str(rmsg), 1, (10, 10, 10))
        board.blit(text1, (rx,130))
        
        cmsg=cmsg+1
        cy=cy+30
        rx=rx+30
        rx1=rx1+30
        rmsg=chr(ord(rmsg)+1)
    
    #image load
    if count==0:
        for s in ships:
        
            image = pygame.image.load("C:\\Python27\\HandsOn\\BattleShip\\"+s+".png").convert()
            board.blit(image, (pos[a][0],pos[a][1]))
            
            a=a+1
        showBoard(ttt,board)

    
    if count<5:
        x=pos[count][0]
        y=pos[count][1]
        print ships[count]

    crashed1=False
    if count==5:
        crashed1=True
    #print crashed1
    
    while not crashed1 and count<5:
        #print crashed1
        for event in pygame.event.get():
           # print 'qqqq'
        #if event.type is QUIT:
            if event.type==pygame.QUIT:
                crashed1=True
                pygame.quit()
                quit()
                
            #running = 0
            if event.type==pygame.MOUSEBUTTONDOWN:
                px, py = pygame.mouse.get_pos()
                img=pygame.image.load("C:\\Python27\\HandsOn\\BattleShip\\"+ships[count]+".png").convert()
                imgWidth=img.get_rect().size[0]
                imgHeight=img.get_rect().size[1]
                size=imgWidth/30
                print 'o:',x,y,imgWidth,imgHeight
                if x<=px<=imgWidth+x and y<=py<=imgHeight+y:
                     rotate_img(ships[count],board,x,y)  
                elif 200<=px<=500 and 150<=py<=450:  
                    position_ships(board,img,size,'h')
                    position(board)
        showBoard (ttt, board)
    
        
    

def rotate_img(img,board,x,y):
    global count
    print 'rotate',x,y,count
    image = pygame.image.load("C:\\Python27\\HandsOn\\BattleShip\\"+img+".png").convert()
    imgWidth=image.get_rect().size[0]
    size=imgWidth/30
    print image
    angle=90
    rect=image.get_rect()
    #print 'rect',rect
    #pygame.Surface.fill((0,0,0))
    pygame.draw.rect(board,(250,250,250),(x,y,rect.size[0],rect.size[1]))
    showBoard(ttt,board)
    r=pygame.transform.rotate(image,angle)
    #print r,'r'
    board.blit(r,(x,y))
    position_ships(board,r,size,'v')
    print 'back',count
    position(board)

def position_ships(board,img,size,orn):
     #Create Ready Button
    global count
    
    ornt.append(orn)
    edgeTop=150
    edgeBottom=450
    interval=30
    edgeLeft=200
    edgeRight=500

    corners = []
    for y in range(edgeTop, edgeBottom, interval):
       for x in range(edgeLeft, edgeRight, interval):
           corners.append((x,y))
            #print 'corner', x,y

    #img = pygame.image.load("C:\\Python27\\HandsOn\\BattleShip\\Carrier.png").convert()
    #print corners
    
    crashed1=False
    counter=0
    flag=1
    while not crashed1 and count<5:
        for event in pygame.event.get():
        #if event.type is QUIT:
            if event.type==pygame.QUIT:
                crashed1=True
                pygame.quit()
                quit()
            #running = 0
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                px, py = pygame.mouse.get_pos()
                print 'c:',px,py
                for cx, cy in corners:
                    #print px,py
                    #print 'hereeeeee'
                    if math.hypot(cx-px, cy-py) < math.sqrt(1800):
                        print 'corner:',cx,cy
                           
                        gy=(cx-200)//30
                        gx=(cy-150)//30

                        if myGrid[gx][gy]==None:
                            
                            print 'cord',gx,gy
                            if orn=='h':
                                i=0
                                for i in range(size):
                                    try:
                                        if myGrid[gx][gy+i]==2:
                                            print 'hello'
                                            flag=0
                                            print 'flag h',flag
                                            break
                                        else:
                                            continue
                                    except IndexError:
                                        flag=0
                                    
                                if flag==1:
                                    board.blit(img, (cx,cy))
                                    img_pos.append((cx,cy))
                                    for i in range(size):
                                        if myGrid[gx][gy+i]==None:
                                            myGrid[gx][gy+i]=2
                                            marked.append((gx,gy))
                                        else:
                                            flag=0
                                            print 'flag',flag
                                            break
                                    count=count+1
                                    counter=counter+1
                                    if counter==1:
                                        crashed1=True
                                        return
                                    print counter
                                    break
                                else:
                                    flag=1
                                

                            elif orn=='v':
                                i=0
                              
                                for i in range(size):
                                    try:
                                        if myGrid[gx+i][gy]==2:
                                            flag=0
                                            break
                                        else:
                                            continue
                                    except IndexError:
                                        flag=0
                                        
                                if flag==1:
                                    board.blit(img, (cx,cy))
                                    img_pos.append((cx,cy))
                                    for i in range(size):
                                        if myGrid[gx+i][gy]==None:
                                            myGrid[gx+i][gy]=2
                                            marked.append((gx,gy))
                                        else:
                                            flag=0
                                            print 'flag',flag
                                            break
                                    count=count+1
                                    counter=counter+1
                                    if counter==1:
                                        crashed1=True
                                        return
                                    print counter
                                    break        
                                else:
                                    flag=1
                                      

                            
                       
                            
                        else:
                            print 'here'
                            if event.type==pygame.MOUSEBUTTONDOWN:
                                px, py = pygame.mouse.get_pos()
                                print 'c:',px,py
                            #continue
                                   
                            
                       
                   
            showBoard (ttt, board)

def ready_btn(board):
    print myGrid  
    pygame.draw.rect(board,(0,0,0),(550,500,100,30),2)
    font = pygame.font.Font(None, 24)
    text = font.render('READY', 1, (10, 10, 10))
    board.blit(text, (570,510))
    crashed=False
    while not crashed and count==5:
        
        for event in pygame.event.get():
        #if event.type is QUIT:
            if event.type==pygame.QUIT:
                crashed=True
                pygame.quit()
                quit()
            #running = 0
            if event.type==pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print str(mouseX)+' '+str(mouseY)
                if 550<=mouseX<=650 and 500<=mouseY<=600:
                    return
        pygame.display.update()
         # update the display
        showBoard (ttt, board)

def clickBoard(board1):
	(mouseX, mouseY) = pygame.mouse.get_pos()
	if(not(600<=mouseX<=900 and 150<=mouseY<=450)):
		return
	edgeTop=150
	edgeBottom=450
	interval=30
	edgeLeft=600
	edgeRight=900

	corners = []
	for y in range(edgeTop, edgeBottom, interval):
		for x in range(edgeLeft, edgeRight, interval):
			corners.append((x,y))
	for cx, cy in corners:
						#print px,py
						#print 'hereeeeee'
		if math.hypot(cx-mouseX, cy-mouseY) < math.sqrt(1800):
			print 'corner:',cx,cy
			return cx,cy


    
def drawMove(board,x,y,res,ttt):
    cx=(x*30)+200
    cy=(y*30)+150
    if res=='miss':
        pygame.draw.circle(board,(0,0,0),((cx+15),(cy+15)),15)
    elif res=='hit':
        pygame.draw.line (board, (0,0,0), (cx,cy),(cx + 30,cy+30), 2)
        pygame.draw.line (board, (0,0,0), (cx+30,cy),(cx,cy+30), 2)
    showBoard(ttt,board)


def enemy(d,x,y,board1,ttt):
    print 'in enemy'
    px=(x-600)//30
    py=(y-150)//30
    #string=d.split(' ')
    if d=='miss':
        Enemygrid[px][py]=0
        pygame.draw.circle(board1,(0,0,0),((x+15),(y+15)),15)
    elif d=='hit':
        Enemygrid[px][py]=1
        pygame.draw.line (board1, (0,0,0), (x,y),(x + 30,y+30), 2)
        pygame.draw.line (board1, (0,0,0), (x+30,y),(x,y+30), 2)

    print d
    showBoard(ttt,board1)



def threaded(c,board1,ttt):
    flag=1
    global prev_x,prev_y
    print 'in threaded'
    while True:
        # data received from client
        data = c.recv(1024)
        print data
        s=data.split(' ')

        if(s[2]!='first'):
            enemy(s[2],prev_x,prev_y,board1,ttt)
        
        board_pos_x=int(s[0])
        prev_x=board_pos_x
        board_pos_y=int(s[1])
        prev_y=board_pos_y
        grid_pos_x=(board_pos_x-600)//30
        grid_pos_y=(board_pos_y-150)//30
        print str(myGrid[grid_pos_x][grid_pos_y])
        if(myGrid[grid_pos_x][grid_pos_y]==2):
            myGrid[grid_pos_x][grid_pos_y]=1
            result='hit'
            flag=0
            #drawMove(board1,grid_pos_x,grid_pos_y,result)
        elif(myGrid[grid_pos_x][grid_pos_y]==None):
            myGrid[grid_pos_x][grid_pos_y]=0
            result='miss'
            flag=0
        print str(grid_pos_x)+str(grid_pos_y)+str(myGrid[grid_pos_x][grid_pos_y])+result
        if flag==0:
            drawMove(board1,grid_pos_x,grid_pos_y,result,ttt)
        if not data:
            print('Bye')
             
            # lock released on exit
            #print_lock.release()
            break

        # reverse the given string from client
        #data = raw_input('Enter msg:')
        print('Enter attck pos')
        crashed=False
        while not crashed:
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        crashed=True
                    if event.type is MOUSEBUTTONDOWN:
                        x,y=clickBoard(board1)
                        if(x and y):
                            print 'back from move'
                            c.send(str(x)+' '+str(y)+' '+result)
                            return
        # send back reversed string to client
        #c.send(data)'''
 
    # connection closed
    #c.close()


# initialize pygame and our window
pygame.init()
ttt = pygame.display.set_mode ((1100, 600))
pygame.display.set_caption ('BattleShip')

# create the game board
board = initBoard (ttt)

position(board)
print 'In Main'
ready_btn(board)
print 'In Main again'
board1=display_boards(ttt)

# main event loop
#running = 1
crashed=False

#while (running == 1):
while not crashed:
    c, addr = s.accept()     
    print 'Got connection from', addr
    showBoard (ttt, board1)
   # send a thank you message to the client. 
    c.send('Thank you for connecting')
    for event in pygame.event.get():
        #if event.type is QUIT:
        if event.type==pygame.QUIT:
            crashed=True

            #running = 0
        #print_lock.acquire()
        #start_new_thread(threaded,(c,board1,ttt))
            
         # update the display
        print 'before'
        threaded(c,board1,ttt)
        showBoard (ttt, board1)
        print 'after'
        #print_lock.release()
      
c.close()
pygame.quit()
quit()
