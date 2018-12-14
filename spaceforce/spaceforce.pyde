#Space Force Game 
# Alex Petriv Github repository: "https://github.com/alexpetriv/CSproject/tree/master/spaceforce"


import os, random, time
add_library('minim')
path = os.getcwd()
player = Minim(this)


class SpaceCraft:
    def __init__(self,x,y,r,g):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.vx=0
        self.vy=0
        self.img = loadImage(path+"/images/"+img)

    
    def display(self):
        stroke(255)
        noFill()
        ellipse(self.x,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        


class Game: #game class
    def __init__(self,w,h,l):
        self.w=w
        self.h=h
        self.l=l #board line along which the player's space craft will be moving
        self.img = loadImage(path+"/images/space5120x800.jpg")
        
        
    def display(self):
        image(self.img,0,0)
        stroke(255)
        line(self.l,0,self.l,self.h)
        line(self.l+1000,0,self.l+1000,self.h)
        
s = Game(1280,800,100)

def setup():
    size(s.w, s.h)
    background(0)

def draw():
    background(0)
    s.display()
















        
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
