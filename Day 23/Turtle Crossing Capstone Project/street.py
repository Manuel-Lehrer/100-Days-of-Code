from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Street (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        for i in range(2):
            if i == 1:
                y = -200
            else:
                y = 200
            self.goto(300, y)
            self.setheading(180)
            self.pensize(10)
            for stripes in range(10):
                self.pendown()
                self.forward(50)
                self.penup()
                self.forward(50)

        self.pensize(3)
        self.color("white")
        self.penup()
        self.goto(-300, -100)
        self.pendown()
        self.goto(300, -100)
        self.penup()
        self.goto(300, 100)
        self.pendown()
        self.goto(-300, 100)

        self.penup()
        self.goto(300, 0)
        self.pensize(45)
        self.color("DeepSkyBlue")
        self.pendown()
        self.goto(-300, 0)
        self.penup()
        self.goto(-300, -23)
        self.pensize(10)
        self.color("coral4")
        self.pendown()
        self.goto(300, -23)
        self.penup()
        self.goto(-300, 23)
        self.pendown()
        self.goto(300, 23)
