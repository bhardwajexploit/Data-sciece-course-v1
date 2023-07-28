from random import randint
import pgzrun

WIDTH=1000
HEIGHT=500
class Player(Actor):
    speed=5
    def player_cntrl(self):
          
            if keyboard.left:
                self.x -=self.speedp
            if keyboard.right:
                self.x +=self.speed
            if keyboard.down:
                self.y +=self.speed
            if keyboard.up:
                self.y -=self.speed
            if keyboard.space:
                self.angle +=self.speed
            



class Enemy(Actor):
    speed=2
    def enemy_cntrl(self,p):
        if p.x>self.x:
            self.x +=self.speed
        if p.x<self.x:
            self.x -=self.speed
        if p.y>self.y:
            self.y +=self.speed
        if p.y<self.y:
            self.y -=self.speed
        if self.collderect(p):
                exit()




class Fruit(Actor):
    x=randint(50,WIDTH-50)
    y=randint(50,HEIGHT-50)

    def relocate(self):
        self.x=randint(50,WIDTH-50)
        self.y=randint(50,HEIGHT-50)
        


