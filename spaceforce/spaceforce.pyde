#Space Force Game 
# Alex Petriv Github repository: "https://github.com/alexpetriv/CSproject/tree/master/spaceforce"

#added enemyship image, background image
#line(x,y,x1,y1)


import os, random, time
add_library('minim')
path = os.getcwd()
player = Minim(this)



class Spacecraft:
    def __init__(self,x,y,r,l):
        self.x=x
        self.y=y
        #radius of the eclipse
        self.r=r
        self.l=l
        self.vx=0
        self.vy=0
        # self.img = loadImage(path+"/images/"+img)

    def display(self):
        stroke(255)
        noFill()
        ellipse(self.x+self.r,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        line(self.x,self.y-self.r,self.l,self.y+self.r)

class Myship(Spacecraft):
    def __init__(self,x,y,r,l):
        Spacecraft.__init__(self,x,y,r,l)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False}

# game class
class Game:
    def __init__(self,w,h,l):
        self.w=w
        self.h=h
        # board line along which the player's space craft will be moving
        self.l=l
        self.img = loadImage(path+"/images/space2560x800.jpg")
        self.myplayer=Myship(l,h/2,35,self.l)
        
    def display(self):
        image(self.img,0,0)
        stroke(255)
        #line along which the player will be moving
        line(self.l,0,self.l,self.h)
        line(self.l+1000,0,self.l+1000,self.h)
        self.myplayer.display()
        
s = Game(1280,800,100)

def setup():
    size(s.w, s.h)
    background(0)

def draw():
    background(0)
    s.display()


def keyPressed():
    if keyCode == LEFT:
        s.myplayer.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        s.myplayer.keyHandler[RIGHT] = True
    elif keyCode == UP:
        s.myplayer.keyHandler[UP] = True
    elif keyCode == DOWN:
        s.myplayer.keyHandler[DOWN] = True
def keyReleased():
    if keyCode == LEFT:
        s.myplayer.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        s.myplayer.keyHandler[RIGHT] = False
    elif keyCode == UP:
        s.myplayer.keyHandler[UP] = False
    elif keyCode == DOWN:
        s.myplayer.keyHandler[DOWN] = False













        
        # frameRate(60)
        # background(230)
        # image(self.img,0,0) #self.w,self.h
        # stroke(255)
        # strokeWeight(2)
        # line(100,0,100,700)
        # line(1110,0,1100,700)
        
        
# s = SpaceForce(1280,700)

# def setup():
#     background(255)
#     size(s.w,s.h)


# def draw():
#     background(255)
#     s.display()



#Need to create the following objects:
#spacecraft, meteoroid, enemy spacecraft, boss spacecraft, health coin
#Create a scorecount: determined by the time the player was able to survive
#Create a health bar or counter for the player, enemies and meteoroids
#Player's space craft will be shooting when a player presses "Space Bar" 
