print(67)
import turtle
paper = turtle.Screen()
turtle.colormode(255)

import random
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255) 

def instagram(x,y):
    paper.bgcolor((r,g,b))
    turtle.colormode(255)


paper.onclick(instagram)
turtle.done()