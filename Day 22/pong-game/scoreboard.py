from turtle import Turtle


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score_p1 = 0
        self.score_p2 = 0
        self.color("white")
        self.up()
        self.speed(0)
        self.goto(0, 270)
        self.print_score()

    def print_score(self):
        self.write(f"Score = {self.score_p1}:{self.score_p2}", align="center", font=('Courier', 20, 'normal'))

    def update_score_p1(self):
        self.clear()
        self.score_p1 += 1
        self.print_score()

    def update_score_p2(self):
        self.clear()
        self.score_p2 += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align="center", font=('Courier', 20, 'normal'))
        self.goto(0, -100)
        if self.score_p1 > self.score_p2:
            self.goto(0, -100)
            self.write("PLAYER 1 WON THE GAME", False, align="center", font=('Courier', 20, 'normal'))
        else:
            self.write("PLAYER 2 WON THE GAME", False, align="center", font=('Courier', 20, 'normal'))
