from turtle import*

pencolor('yellow')
pensize(2)
bgcolor('black')
speed("fastest")

for i in range(5):
    fd(100)
    rt(360/5)
    for i in range(5):
        pencolor("red")
        fd(50)
        rt(360/5)
        for i in range(5):
            fd(150)
            rt(360/5)


    

mainloop()