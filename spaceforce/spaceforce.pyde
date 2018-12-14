#Space Force Game 
# Alex Petriv Github repository: "https://github.com/alexpetriv/CSproject/tree/master/spaceforce"

#added enemyship image, background image
#line(x,y,x1,y1)


import os, random, time
add_library('minim')
path = os.getcwd()
player = Minim(this)



class Spacecraft:
    def __init__(self,x,y,r,l,img,w,h):
        self.x=x
        self.y=y
        self.r=r
        self.l=l
        self.vx=0
        self.vy=0
        self.img = loadImage(path+"/images/"+img)
        self.w=w
        self.h=h
        # self.F=F
       
    def update(self):      
        self.x += self.vx
        self.y += self.vy


    def display(self):
        self.update()
        stroke(255)
        noFill()
        ellipse(self.x+self.r,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        image(self.img,self.x,self.y-self.r,self.r*2,self.r*2)

class Myship(Spacecraft):
    def __init__(self,x,y,r,l,img,w,h):
        Spacecraft.__init__(self,x,y,r,l,img,w,h)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False}
        
    def update(self):
        if self.keyHandler[UP]:
            self.vy = -10
        elif self.keyHandler[DOWN]:
            self.vy = 10
        else:
            self.vx = 0
            self.vy = 0
        
        self.x += self.vx
        self.y += self.vy
        
        if self.x-self.r < 0:
            self.x = self.r
            
class Enemy(Spacecraft):
        def __init__(self,x,y,r,l,img,w,h):
            Spacecraft.__init__(self,x,y,r,l,img,w,h)
        def update(self):
            self.x += self.vx
            self.y += self.vy

class Enemyboss(Spacecraft):
        def __init__(self,x,y,r,l,img,w,h): 
            Spacecraft.__init__(self,x,y,r,l,img,w,h)
        def update(self):
            self.x += self.vx
            self.y += self.vy

# game class
class Game:
    def __init__(self,w,h,l):
        self.w=w
        self.h=h
        # board line along which the player's space craft will be moving
        self.l=l
        self.img = loadImage(path+"/images/space2560x800.jpg")
        self.myplayer=Myship(l,h/2,35,self.l,"playership1.png",100,70)
        self.enemy = Enemy(l+1000,h/3,35,self.l+100,"enemyship1.png",100,70)
        self.enemyboss = Enemyboss(l+1000,h/2,105,self.l+100,"enemyboss1.png",300,210)
        
    def display(self):
        image(self.img,0,0)
        stroke(255)
        #line along which the player will be moving
        line(self.l,0,self.l,self.h)
        line(self.l+1000,0,self.l+1000,self.h)
        self.myplayer.display()
        self.enemy.display()
        self.enemyboss.display()
        
s = Game(1280,800,50)

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
