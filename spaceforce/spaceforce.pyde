#Space Force Game 
# Alex Petriv Github repository: "https://github.com/alexpetriv/CSproject/tree/master/spaceforce"

import os, random, time
add_library('minim')
path = os.getcwd()
player = Minim(this)

# Created a space craft class that will we used to create my spaces ship and enemies. Arguments include location, radius, l = line on which
# the space craft gets created; emage, width and height

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
       
       # Place where I have speed (x and y directions) as a function of velocity. 
    def update(self):  
        self.x += self.vx
        self.y += self.vy

        # Place where I show which image for spacecraft should be located where.
    def display(self):
        self.update()
        image(self.img,self.x,self.y-self.r,self.r*2,self.r*2)

#The class that represents the players own ship. Includes same attributes as the space craft class. Inherits some properties of the Space craft.
class Myship(Spacecraft):
    def __init__(self,x,y,r,l,img,w,h):
        Spacecraft.__init__(self,x,y,r,l,img,w,h)
        #Show initial values for my keys. These will be used to control the space ship.
        self.keyHandler={LEFT:False, RIGHT:False, UP:False, DOWN:False, 'SPACE':False}
        self.recoil = 0
        self.bullets = []
        
    def update(self):
        self.collision()
        if self.recoil > 0:
            self.recoil -= 1
        for i in self.bullets:
            i.display()
        
        #Increasing velocity only along the y axis by pressing either UP or DOWN arrows.
        if self.keyHandler[UP]:
            self.vy = -10
        elif self.keyHandler[DOWN]:
            self.vy = 10
        else:
            self.vx = 0
            self.vy = 0
        #Shooting. Allow to do it in an interval defined by recoil var. Otherwise it would be able to shoot continuosly and it would be to easy to win.
        if self.keyHandler['SPACE'] and self.recoil == 0:
            self.bullets.append(Bullet(self.x,self.y,1))
            self.recoil = 15

        self.x += self.vx
        self.y += self.vy
        
        if self.y <= self.r:
            self.y = self.r
        elif self.y >= 800-self.r:
            self.y = 800 - self.r


# Define collision case when the enemy collidues with you and you lose the game.
    def collision(self):
        for a in s.enemies:
            if ((self.x+self.r-a.x-a.r)**2+(self.y+self.r-a.y-a.r)**2)**0.5 <= self.r+a.r:
                print('collide')
                s.status = 0
        #Enemy space craft as a class inherited from Spacecraft. Shares same attributes initially.
class Enemy(Spacecraft):
        def __init__(self,x,y,r,l,img,w,h):
            Spacecraft.__init__(self,x,y,r,l,img,w,h)
            self.y1 = self.r+1
            #Define the trajectories along which the enemies should be moving. Also they would move at randomly selected velocities.
            self.var = [400,450,500,550]
            self.y2 = self.var[random.randint(0,3)]
            self.vy = random.randint(-7,7)
            self.vx = random.randint(-7,-2)
            
            #Create bulles list to account for bulles. Use recoil to control the rate at which the enemy will be shooting.
            self.bullets = []
            self.recoil = 27
            
            
        def update(self):
            self.recoil -=1
            self.doging()
            self.x += self.vx
            self.y += self.vy
            if self.y <= self.r:
                self.y = self.r
            elif self.y >= 800-self.r:
                self.y = 800 - self.r
            
                #lose condition    
            if self.x <= -75:
                del s.enemies[:]
                s.kills -=1
                if s.kills < 0:
                    s.status = 0
                
                #Creating new enemies once others get killed or deleted
            if len(s.enemies) == 0:
                s.enemies.append(Enemy(s.l+1100,s.h/random.randint(1,8),35,s.l+100,"enemyship1.png",100,70))
            if self.recoil == 0:    
                self.bullets.append(Bullet(self.x,self.y,-1))
                self.recoil = 27
            for i in self.bullets:
                i.display()
                
        def doging(self):
            if self.y <= self.y1:
                self.vy = -self.vy
            elif self.y >= self.y2:
                self.vy = -self.vy
            
            
            
#Created a class for enemy boss which shares same attributes as the class spacecraft.
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
             
 #Bullet class in which i define dimensions and image for bullets.   
class Bullet:
    def __init__(self, x,y,v):
        self.x = x+100*v
        self.y = y-6
        self.v = v
        
    def display(self):
        self.update()
        fill(255,255,0)
        rect(self.x,self.y,45,10,9)
        
    def update(self): ####update

        if self.v == 1:
            self.x += 8
        else:
            self.x -= 8
        
        #COndition to remove enemies one the bullets hit them
        for k in s.enemies:
            if self.v != -1 and k.x-1<=self.x+40<=k.x+100 or k.x-1<=self.x<=k.x+100 or k.x-1<=self.x+15<=k.x+100 or k.x-1<=self.x+30<=k.x+100 or k.x-1<=self.x+20<=k.x+100:
                if k.y-50<=self.y<=k.y+70 :
                    self.x = 5000
                    s.enemies.remove(k)
                    s.kills +=1
                    if len(s.enemies) == 0:
                        s.enemies.append(Enemy(s.l+1230,s.h/3,35,s.l+100,"enemyship1.png",100,70))
                        
                                        
        if s.myplayer.x <=self.x<=s.myplayer.x +100 and s.myplayer.y-70<=self.y <= s.myplayer.y+70:
            s.status = 0
        
#Pic for a boss and condition to give a boss every time you kill 5 smaller enemies.
        if s.kills > 1 and s.kills%5 == 0: #BOSS
            for k in s.enemies:
                s.enemies.remove(k)
                s.enemies.append(Enemy(s.l+1000,s.h/2,105,s.l+100,"enemyboss1.png",300,210))

# game class in which i define the main settings of the game.
class Game:
    def __init__(self,w,h,l):
        self.kills = 0 
        self.status = 1
        self.w=w
        self.frames = 0
        self.h=h
        # board line along which the player's space craft will be moving
        self.l=l
        self.img = loadImage(path+"/images/space2560x800.jpg")
        self.myplayer=Myship(l,h/2,35,self.l,"playership1.png",100,70)
        self.enemies = []
        self.enemies.append(Enemy(l+1230,h/3,35,self.l+100,"enemyship1.png",100,70))
        self.enemyboss = Enemyboss(l+1230,h/2,105,self.l+100,"enemyboss1.png",300,210)
        
    def display(self):
        
        #image(self.img,-500,0)
        stroke(255)
        #line along which the player will be moving
        # line(self.l,0,self.l,self.h)
        # line(self.l+1000,0,self.l+1000,self.h)
        self.myplayer.display()
        for k in self.enemies:
            k.display()
        self.enemyboss.display()
        

s = Game(1280,800,50)

def setup():
    size(s.w, s.h)
    background(0)
#Move frames and create a background picture (consits of two images). Gives a continuous loop effect. 
def draw():    
    if s.status == 1:
        s.frames +=15
        s.frames = s.frames%2560
    
        background(0)
        image(s.img,-s.frames,0)
        image(s.img,2560-s.frames,0)
        s.display()
        textSize(35)
        fill(255)
        text(s.kills,10,32)
    elif s.status == 0:
        background(0)
        textSize(45)
        fill(255)
        text('You Lost, mate', 350,200)



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
