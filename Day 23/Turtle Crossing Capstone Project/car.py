from turtle import Turtle
import random

COLORS = ["red", "orange", "DarkBlue", "purple", "black", "DeepSkyBlue", "CornFlowerBlue", "BlueViolet", "Azure2"]
STARTING_MOVE_DISTANCE = 4
MOVE_INCREMENT = 3


class Car (Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.penup()
        self.setpos(cords)
        self.setheading(180)
        self.speed_cars = STARTING_MOVE_DISTANCE

    def move_car(self):
        self.forward(self.speed_cars)

    def next_level(self):
        self.speed_cars += MOVE_INCREMENT
