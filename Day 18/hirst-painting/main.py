# import colorgram
#
# colors = colorgram.extract('image.jpeg', 10)
#
#
# all_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     rgb_tuple = (r, g, b)
#     all_colors.append(rgb_tuple)
#
# print(all_colors)
import turtle
from turtle import Turtle
import random
color_list = [(239, 221, 113), (18, 111, 193), (223, 60, 95), (235, 150, 76), (116, 147, 208), (143, 88, 50)]
t = Turtle()
turtle.colormode(255)
t.speed(0)
t.hideturtle()


def one_row():
    for y in range(0, 10):
        t.color(random.choice(color_list))
        t.begin_fill()
        t.circle(18)
        t.end_fill()
        t.up()
        t.forward(50)
        t.down()


def turn_around():
    t.up()
    t.left(180)
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.down()


t.up()
t.setheading(225)
t.forward(300)
t.setheading(0)
t.down()


for i in range(0, 10):
    one_row()
    turn_around()
