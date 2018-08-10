#PythonDraw.py
import turtle
#from turtle import * #turtle.goto()->goto()
#import turtle as tu #turtle.goto()->tu.goto()
turtle.setup(650,350,200,200)
#turtle.setup(width,height,starx,stary)
#turtle.setup(width,height)
#turtle.goto(x,y)
#turtle.forward(d) back(d) circle(r[,angle]) 
#turtle.setheading(angle) turtle.left(angle) turtle.right(angle)
#turtle.colormode(mode) mode=1.0 mode=255
turtle.penup()
#turtle.penup() pendown() pensize() pencolor("purple"|0.63,0.13,0.94|(0.63,0.13,0.94))
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)  
turtle.pencolor("purple")
turtle.seth(-40)
#for i in range(4) #i=0 1 2 3
for i in range(4):
	turtle.circle(40,80)
	turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()