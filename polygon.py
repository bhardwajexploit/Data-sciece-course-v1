from turtle import *

def sqaure():
    for i in range(4):
        forward(100)
        right(90)

def pentagon():
    for i in range(6):
      forward(100)
      right(72)





#calling
sqaure()
pentagon()
goto(200,0)
sqaure()
pentagon()

hideturtle()
mainloop()