from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self, speed=1):
        super().__init__(shape="circle")
        self.color("white")
        self.speed(speed)
        self.penup()
        self.xmovement = random.choice([10, -10])
        self.ymovement = random.choice([10, -10])
        self.move_speed = 0.1

    def move(self):
        new_coord = (self.xcor() + self.xmovement, self.ycor() + self.ymovement)
        self.goto(new_coord)

    def ybounce(self):
        self.ymovement *= -1

    def xbounce(self):
        self.xmovement *= -1
        self.move_speed *= 0.9

    def change_turn(self):
        self.goto(0, 0)
        self.xmovement *= -1
        self.move_speed = 0.1
