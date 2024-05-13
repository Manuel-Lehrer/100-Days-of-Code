import turtle
from turtle import Turtle, Screen
import random

t = Turtle()

t.shape("square")
t.color("blue")

t.speed(0)
#t.pensize(1)
turtle.colormode(255)
directions = [90, 180, 270, 360]


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


for i in range(180):
    t.circle(200)
    t.right(2)
    t.color(random_color())


# play = True
# while play == True:
#     t.forward(25)
#     t.left(random.choice(directions))
#     t.color(random_color())


    # t.color(random.random(), random.random(), random.random())
    #alternative without colormode

# def shape():
#     for i in range(n):
#         t.forward(100)
#         t.left(360/n)
#
#
# for n in range(3, 10):
#     shape()
#     t.color(random.random(), random.random(), random.random())














# for i in range(20):
#     t.forward(10)
#     t.up()
#     t.forward(10)
#     t.down()









screen =Screen()
screen.exitonclick()