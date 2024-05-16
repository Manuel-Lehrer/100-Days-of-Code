import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_guessed = 0

printer = turtle.Turtle()
printer.hideturtle()
printer.up()

data = pandas.read_csv("50_states.csv")

states_names = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()

    if answer == "Exit":
        missed_states = [state for state in states_names if state not in guessed_states]
        missed_states_data = pandas.DataFrame(missed_states)
        missed_states_data.to_csv("missed_states_data.csv")
        break
    if answer in states_names:
        guessed_states.append(answer)
        x_value = data.loc[data["state"] == answer, "x"].values[0]
        y_value = data.loc[data["state"] == answer, "y"].values[0]
        printer.goto(x_value, y_value)
        printer.write(answer)



