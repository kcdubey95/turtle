import random
from turtle import Turtle,Screen
from random import Random

myscreen=Turtle()


def shap(side):
    angal = 360/side
    for _ in range(side):
        myscreen.forward(100)
        myscreen.right(angal)


for i in range(3, 11):
    myscreen.color("red")
    shap(i)


diraction= [0, 90, 180, 270]
for _ in range(200):
    myscreen.forward(30)
    myscreen.pensize(15)
    myscreen.setheading(random.choice(diraction))

screen = Screen()
screen.exitonclick()