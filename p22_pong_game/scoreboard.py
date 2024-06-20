from turtle import Turtle

FONT = ("ariel", 30, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 240)
        self.lscore = 0
        self.rscore = 0
        self.write(f"{self.lscore}         {self.rscore}", align=ALIGNMENT, font=FONT)

    def score_update(self, player):
        if player == "left":
            self.lscore += 1
        else:
            self.rscore += 1

        self.clear()
        self.write(f"{self.lscore}         {self.rscore}", align=ALIGNMENT, font=FONT)


class Partition(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pen({"pensize": 7, "pencolor": "white"})
        self.penup()
        self.goto(0, 300)
        self.draw()

    def draw(self):
        self.setheading(270)
        while self.ycor() > -320:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
