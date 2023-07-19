from turtle import *

def Polygone(sides,length,color,width):
    pencolor(color)
    pensize(width)
    for i in range(sides):
        forward(length)
        right(360/sides)
    
# callling
Polygone(6,100,'black',10)
goto(900,500)
mainloop()