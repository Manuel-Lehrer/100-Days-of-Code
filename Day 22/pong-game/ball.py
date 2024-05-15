from turtle import Turtle


class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.color("chartreuse")
        self.shape("circle")
        self.up()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def ball_ofr(self):
        self.setpos(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1
