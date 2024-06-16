from turtle import Turtle, Screen
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_LENGTH = 15
BODY_COLOR = "white"
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_block(position)

    def add_block(self, position):
        new_box = Turtle(shape="square")
        new_box.penup()
        new_box.color(BODY_COLOR)
        new_box.goto(position)
        self.blocks.append(new_box)

    def move(self):
        for index in range(len(self.blocks)-1, 0, -1):
            x_axis = self.blocks[index-1].xcor()
            y_axis = self.blocks[index-1].ycor()
            self.blocks[index].goto(x_axis, y_axis)
        self.head.forward(MOVE_LENGTH)

    def reset(self):
        for block in self.blocks:
            block.goto(1000, 1000)
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]

    def size_grow(self):
        self.add_block(self.blocks[-1].position())

    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)
