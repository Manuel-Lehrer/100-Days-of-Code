from turtle import Turtle

FONT = ('Courier', 20, 'normal')

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_snake.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.up()
        self.speed(0)
        self.goto(0, 260)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}", False, align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.print_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore_snake.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.print_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", False, align="center", font=('Courier', 20, 'normal'))
