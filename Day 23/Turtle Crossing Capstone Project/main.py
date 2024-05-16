import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
from street import Street
import random

AMOUNT_OF_CARS = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("DarkGrey")
screen.title("Turtle about to get squished")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
scoreboard.print_level()
street = Street()

all_cars = []

for cars in range(1, AMOUNT_OF_CARS):
    new_car = Car((random.randint(0, 600), (75 * random.randint(-3, 3))))
    all_cars.append(new_car)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(player.move, "w")
    for cars in all_cars:
        cars.move_car()

    for cars in all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 279:
        player.reset()
        scoreboard.update_level()
        for cars in all_cars:
            cars.next_level()

    for cars in all_cars:
        if cars.xcor() < -320:
            cars.setx(320)


screen.exitonclick()
