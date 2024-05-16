from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210, 260)
        self.level = 1
        self.print_level()

    def print_level(self):
        self.write(f"Level = {self.level}", False, align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.print_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align="center", font=FONT)
