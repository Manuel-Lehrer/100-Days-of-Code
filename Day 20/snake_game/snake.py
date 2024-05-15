from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(20, 0), (0, 0), (0, -20)]


class Snake:

    def __init__(self):
        self.snake_bodies = []
        self.create_snake()
        self.head = self.snake_bodies[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        new_square = Turtle("square")
        new_square.color("green")
        new_square.up()
        new_square.goto(position)
        self.snake_bodies.append(new_square)

    def extend(self):
        self.add_body(self.snake_bodies[-1].position())

    def move(self):
        for bodies_num in range(len(self.snake_bodies) - 1, 0, -1):
            x_cor = self.snake_bodies[bodies_num - 1].xcor()
            y_cor = self.snake_bodies[bodies_num - 1].ycor()
            self.snake_bodies[bodies_num].goto(x_cor, y_cor)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for bodies in self.snake_bodies:
            bodies.goto(1000,1000)
        self.snake_bodies.clear()
        self.create_snake()
        self.head = self.snake_bodies[0]
