from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.lvl_count = 0
        self.write(f"Level : {self.lvl_count}", align="left", font=FONT)

    def next_level(self):
        self.lvl_count += 1
        self.clear()
        self.write(f"Level : {self.lvl_count}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)