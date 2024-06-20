from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.color("purple")
        self.goto_starting_line()
        self.setheading(90)

    def forward_move(self):
        self.forward(MOVE_DISTANCE)

    def goto_starting_line(self):
        self.goto(STARTING_POSITION)
