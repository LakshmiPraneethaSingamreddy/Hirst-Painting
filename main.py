import turtle
from turtle import Turtle
import random
timmy=Turtle()
turtle.colormode(255)
timmy.hideturtle()
colors=[(226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96), (113, 174, 215), (244, 227, 95), (173, 20, 41), (233, 79, 51), (224, 126, 156), (118, 184, 130), (11, 172, 207), (165, 151, 25), (13, 58, 148), (83, 37, 23), (128, 37, 27), (37, 129, 78), (42, 192, 160), (14, 39, 92), (129, 238, 190), (244, 162, 151), (235, 162, 181), (100, 101, 186), (127, 214, 239), (66, 77, 38), (74, 31, 46), (20, 93, 54), (160, 175, 234), (254, 238, 0), (26, 65, 48), (251, 7, 38)]
k=-200
timmy.penup()
timmy.setpos(-200, k)
timmy.speed("fastest")
for _ in range(0,10):
    for _ in range(0,10):
        timmy.pendown()
        timmy.dot(20,random.choice(colors))
        timmy.penup()
        timmy.forward(50)
    k=k+50
    timmy.setpos(-200, k)






screen=turtle.Screen()
screen.exitonclick()
