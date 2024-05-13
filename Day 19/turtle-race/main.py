import random
import turtle
from turtle import Turtle, Screen
from random import randint

race_start = False
screen = Screen()
screen.setup(width=1000, height=800)

choice = screen.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow","green", "blue", "purple"]

# t = Turtle("turtle")
# t.up()
# t.goto(-400, -300)
#
# z = Turtle("turtle")
# z.goto(-400, -200)
all_turtles = []


for color in range (1,7):
    new = Turtle("turtle")
    new.color(colors[color-1])
    new.up()
    if color % 2 == 0:
        y = 40 * color

    else:
        y = -40 * color
    new.goto(-400, y)

    all_turtles.append(new)

if choice:
    race_start = True

while race_start:
    for turtles in all_turtles:
        if turtles.xcor() > 250:
            winning_color = (turtles.pencolor())
            if winning_color == choice:
                print(f"You won. The winner was the {winning_color} turtle.")
            else:
                print(f"You lost .The winner was the {winning_color} turtle.")
            race_start = False
        else:
            random_movement = random.randint(0,10)
            turtles.forward(random_movement)








screen.exitonclick()