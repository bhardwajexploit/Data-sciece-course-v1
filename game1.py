import pgzrun
from random import randint

#screen size
HEIGHT=500
WIDTH=1000

#objects

p=Actor('hero')
e=Actor('enemy')
c=Actor('friut')

c.x=randint(50,WIDTH-50)
c.y=randint(50,HEIGHT-50)
p.pos=(WIDTH/2,HEIGHT/2)
e.pos=(-100,HEIGHT/2)

ps=20
es=5
score=0

def draw(): 
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'Score: {score}',(10,10),color='purple')

def update(dt):
   #player control
    global score
    if keyboard.left:
        p.x -=ps
    if keyboard.right:
        p.x +=ps
    if keyboard.down:
        p.y +=ps
    if keyboard.up:
        p.y -=ps
    if keyboard.space:
       p.angle +=ps
       #enemy control 
    if p.x>e.x:
        e.x +=es
    if p.x<e.x:
        e.x -=es
    if p.y>e.y:
        e.y +=es
    if p.y<e.y:
        e.y -=es
    

    #fruit collisiom
    if p.colliderect(c):
        c.x=randint(50,WIDTH-50)
        c.y=randint(50,HEIGHT-50)
        score  +=10
        sounds.clap.play()

       

           

#ggameloop
pgzrun.go()