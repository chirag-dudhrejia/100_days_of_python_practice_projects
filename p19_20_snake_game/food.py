from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.generate_food()

    def generate_food(self):
        x_axis = random.randint(-270, 270)
        y_axis = random.randint(-270, 270)
        self.goto(x_axis, y_axis)