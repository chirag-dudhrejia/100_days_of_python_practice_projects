import turtle
from turtle import Screen, Turtle
import pandas as pd


screen = Screen()
screen.title("U.S. states guessing game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def write_name(state_name, x, y, turt):
    turt.penup()
    turt.hideturtle()
    turt.goto(x, y)
    turt.write(state_name, align="center", font=("arial", 8, "normal"))


data = pd.read_csv("50_states.csv")
guessed_correct = []
remaining_list = data["state"].tolist()

turtle_write = Turtle()
turtle_write.speed(10)
while len(guessed_correct) != len(data):
    name = screen.textinput(title=f"{len(guessed_correct)}/{len(data)} states correct",
                            prompt="What's another state name?")
    name = name.title()

    if name == "Exit":
        break

    if (name in remaining_list) and (name not in guessed_correct[:]):
        guessed_correct.append(name)
        remaining_list.remove(name)
        value = data[data["state"] == name].values.ravel()
        write_name(name, value[1], value[2], turtle_write)

if len(guessed_correct) == len(data):
    turtle_write.goto(0, 0)
    turtle_write.write("Wohoo! You guessed them all.", align="center", font=("ariel", 30, "normal"))
else:
    remaining_states_frame = pd.DataFrame(remaining_list)
    remaining_states_frame.to_csv("states_remain.csv")

turtle.mainloop()
