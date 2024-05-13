from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(25)

def move_backward():
    t.backward(25)

def turn_left():
    t.left(25)

def turn_right():
    t.right(25)

def screen_clear():
    t.home()
    t.clear()




screen.listen()
screen.onkey(key="w", fun = move_forward)
screen.onkey(key="s", fun = move_backward)
screen.onkey(key="a", fun = turn_left)
screen.onkey(key="d", fun = turn_right)
screen.onkey(key="c", fun = screen_clear)
screen.exitonclick()