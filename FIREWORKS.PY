# importing and basics : ) 
import turtle 
import random 
paper = turtle.Screen()
pen = turtle.Turtle() 
paper.bgcolor("black")
pen.speed(0)
pen.pensize(4)
turtle.colormode(255)
# looping fireworks 
for i in range(67):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    pen.color(r,g,b)
   # selecting a random locatian for the fireworks: :)
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    pen.up()
    pen.goto(x,y)
    pen.down()
    # SHAPING 
    r =36
    while r > 0:
        r = r-1 
        youtube =random.randint(67,98)
        pen.forward(youtube)
        pen.backward(youtube)
        pen.right(10)