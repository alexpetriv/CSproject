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
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False, 'SPACE':False}
        self.recoil = 0
        self.bullets = []
        
    def update(self):
        if self.recoil > 0: #### RECOIL COMMENT
            self.recoil -= 1
        for i in self.bullets:
            i.display()
        
        if self.keyHandler[UP]:
            self.vy = -10
        elif self.keyHandler[DOWN]:
            self.vy = 10
        else:
            self.vx = 0
            self.vy = 0

        if self.keyHandler['SPACE'] and self.recoil == 0:
            self.bullets.append(Bullet(self.x,self.y))
            self.recoil = 15

        
        self.x += self.vx
        self.y += self.vy
        
        if self.y <= self.r:
            self.y = self.r
        elif self.y >= 800-self.r:
            self.y = 800 - self.r



    def collision(self):
        pass
            
class Enemy(Spacecraft):
    
    
        def __init__(self,x,y,r,l,img,w,h):
            Spacecraft.__init__(self,x,y,r,l,img,w,h)
            self.y1 = self.r+1
            #self.y2 = [random.randint(0,3)]
            self.var = [400,450,500,550]
            self.y2 = self.var[random.randint(0,3)]
            self.vy = -5
            self.vx = -5
            print self.y1, self.y2
            
            
        def update(self):
            self.doging()
            self.x += self.vx
            self.y += self.vy
            if self.y <= self.r:
                self.y = self.r
            elif self.y >= 800-self.r:
                self.y = 800 - self.r
                
        def doging(self):
            if self.y <= self.y1:
                self.vy = -self.vy
            elif self.y >= self.y2:
                self.vy = -self.vy
            
            
            

class Enemyboss(Spacecraft):
        def __init__(self,x,y,r,l,img,w,h): 
            Spacecraft.__init__(self,x,y,r,l,img,w,h)
        def update(self):
            
            self.x += self.vx
            self.y += self.vy
            if self.y <= self.r:
                self.y = self.r
            elif self.y >= 800-self.r:
                self.y = 800 - self.r
                
class Bullet:
    def __init__(self, x,y):
        self.x = x+100
        self.y = y-6
        
    def display(self):
        self.update()
        fill(255,255,0)
        rect(self.x,self.y,45,10,9)
        
    def update(self): ####update
        self.x += 8


# game class
class Game:
    def __init__(self,w,h,l):
        self.w=w
        self.frames = 0
        self.h=h
        # board line along which the player's space craft will be moving
        self.l=l
        self.img = loadImage(path+"/images/space2560x800.jpg")
        self.myplayer=Myship(l,h/2,35,self.l,"playership1.png",100,70)
        self.enemies = []
        self.enemies.append(Enemy(l+1000,h/3,35,self.l+100,"enemyship1.png",100,70))
        self.enemyboss = Enemyboss(l+1000,h/2,105,self.l+100,"enemyboss1.png",300,210)
        
    def display(self):
        
        #image(self.img,-500,0)
        stroke(255)
        #line along which the player will be moving
        line(self.l,0,self.l,self.h)
        line(self.l+1000,0,self.l+1000,self.h)
        self.myplayer.display()
        for k in self.enemies:
            k.display()
        #self.enemyboss.display()
        
        
        
        
        
        
        
        
        
s = Game(1280,800,50)









def setup():
    size(s.w, s.h)
    background(0)

def draw():
    s.frames +=15
    s.frames = s.frames%2560
    
    background(0)
    image(s.img,-s.frames,0)
    image(s.img,2560-s.frames,0)
    s.display()








def keyPressed():
    if keyCode == 32:
        s.myplayer.keyHandler['SPACE'] = True
    if keyCode == LEFT:
        s.myplayer.keyHandler[LEFT] = True
    elif keyCode == RIGHT:
        s.myplayer.keyHandler[RIGHT] = True
    elif keyCode == UP:
        s.myplayer.keyHandler[UP] = True
    elif keyCode == DOWN:
        s.myplayer.keyHandler[DOWN] = True
    
def keyReleased():
    if keyCode == 32:
        s.myplayer.keyHandler['SPACE'] = False
    if keyCode == LEFT:
        s.myplayer.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        s.myplayer.keyHandler[RIGHT] = False
    elif keyCode == UP:
        s.myplayer.keyHandler[UP] = False
    elif keyCode == DOWN:
        s.myplayer.keyHandler[DOWN] = False
