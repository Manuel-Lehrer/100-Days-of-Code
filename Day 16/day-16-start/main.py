from turtle import *
import random

# Learning and trying out things with the turtle module

t = Turtle()
my_screen = Screen()
my_screen.bgcolor("black")
t.speed(0)


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']


t.hideturtle()
while True:
    for x in range(60, 30000):
        t.pencolor(colors[x % len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(42)




# t.color("yellow")
#
#
# t.width(12)
#
# for i in range(50000000000):
#     t.forward(150)
#     t.right(144)
#     if i % 20 == 0:
#         t.right(80)
#         t.forward(20)
#     if i % 60 == 0:
#         t.right(80)
#         t.forward(200)








# def change_color():
#     R = random.random()
#     B = random.random()
#     G = random.random()
#
#     t.color(R, G, B)
#
#
# t.color("red")

# for i in range(0, 10000000):
#     t.circle(3)
#     t.right(10)
#     t.forward(5)
#
#     if i % 20 == 0:
#         t.forward(10)
#     if i % 25 == 0:
#         t.left(18)
#
#     change_color()


# timmy.shape("turtle")
# timmy.color("blue")


# for i in range(100, 100000, 20):
#     timmy.forward(i)
#     timmy.left(120)
#     if i % 20 == 0:
#         timmy.color("red")
#     elif i % 20 != 0:
#         timmy.color("blue")
#
#
# my_screen = Screen()
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)