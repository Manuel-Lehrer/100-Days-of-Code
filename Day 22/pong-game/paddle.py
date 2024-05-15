from turtle import Turtle


class Paddle (Turtle):
    def __init__(self, cords):
        super().__init__()
        self.color("DeepSkyBlue")
        self.shape("square")
        self.left(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.up()
        self.speed(0)
        self.starting_position(cords)

    def starting_position(self, cords):
        self.setpos(cords)

    def move_up(self):
        self.forward(25)

    def move_down(self):
        self.backward(25)
