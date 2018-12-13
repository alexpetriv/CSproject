#Space Force Game 
# Alex Petriv Github repository: "https://github.com/alexpetriv/CSproject/tree/master/spaceforce"

import os, random, time
add_library('minim')
path = os.getcwd()
player = Minim(this)


#Need to create the following objects:
#spacecraft, meteoroid, enemy spacecraft, boss spacecraft, health coin
#Create a scorecount: determined by the time the player was able to survive
#Create a health bar or counter for the player, enemies and meteoroids
#Player's space craft will be shooting when a player presses "Space Bar" 


class SpaceCraft:
    def __init__ (self,x,y,r,g,img,w,h,F):
        self.x=x
        self.y=y
        self.r=r
        self.g=g
        self.w=w
        self.h=h
        self.f=0
        self.F=F
        self.vx=0
        self.vy=0
        self.dir = 1
        self.img = loadImage(path+"/images/"+img)
    
    # def update(self):
        
    def display(self):
        # self.update()
        stroke(255)
        noFill()
        strokeWeight(5)
        ellipse(self.x-g.x,self.y,2*self.r,2*self.r)
        stroke(0,255,0)
        line(self.x-self.r-g.x,self.g,self.x+self.r-g.x,self.g)

#This class will be used to create meteoroid and coins objects that can damage you or boost your      
class FlyingObject():
    def __init__(self,x,y,r,img,w,h,F):
        self.x=x
        self.y=y
        self.r=r
        self.w=w
        self.h=h
        self.F=F
        self.img = loadImage(path+"/images/"+img)
        
#Player's space craft inherited from SpaceCraft
class Player(SpaceCraft):
    def __init__(self,x,y,r,g,img,w,h,F):
        SpaceCraft.__init__(self,x,y,r,g,img,w,h,F)

#Enemy space craft inherited from SpaceCraft
class Enemy(SpaceCraft):
    def __init__(self,x,y,r,g,img,w,h,F):
        SpaceCraft.__init__(self,x,y,r,g,img,w,h,F)

#Final boss enemy space craft inherited from SpaceCraft
class EnemyBoss(SpaceCraft):
        def __init__(self,x,y,r,g,img,w,h,F):
            SpaceCraft.__init__(self,x,y,r,g,img,w,h,F)

#Meteoroid object is inherited from FlyingObject. This object will fly at constant speed and direction at the player.
#If it hits the player, player's health gets damaged. A meteoroid can also be destroyed by tte player.
class Meteoroid(FlyingObject):
    def __init__(self,x,y,r,img,w,h,F):
        FlyingObject.__init__(self,x,y,r,img,w,h,F)

#Coin object is inherited from FlyingObject. This object will fly at constant speed and direction at the player.
#If it hits the player, player's health gets damaged. A meteoroid can also be destroyed by tte player.
class Coin(FlyingObject):
    def __init__(self,x,y,r,img,w,h,F):
        FlyingObject.__init__(self,x,y,r,img,w,h,F)
        
        
class Game:
        def __init__ (self,w,h):#add initialpos later)
            self.w=w
            self.h=h
            #self.initialpos=initialpos #initial pos will indicate where the space craft appears on the xy axis
            #self.gameOver = player.loadFile(path+"/sounds/gameover.wav")
            self.musicgame = player.loadFile(path+"/sounds/musicgame.mp3") #Background music that will start playing once the game begins. 
            self.musicstart = player.loadFile(path+"/sounds/musicstart.mp3")
            self.musicstart.play()

g = Game(1280,720)
