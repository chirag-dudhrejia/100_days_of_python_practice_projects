import random
import turtle
from turtle import Turtle, Screen
import colorgram


def extract_colors(img_name):
    colors_list = colorgram.extract(img_name, 30)
    colors_rgb = []
    for color in colors_list:
        rgb = color.rgb
        rgb_tuple = (rgb.r, rgb.g, rgb.b)
        colors_rgb.append(rgb_tuple)
    return colors_rgb


my_turtle = Turtle()
turtle.colormode(255)
my_turtle.speed(20)
my_turtle.penup()
my_turtle.hideturtle()

my_screen = Screen()
my_screen.setup(700, 700)

# To fetch color from any user defined image
# colors = extract_colors("phaidon-going-once-contemporary-masters-900x450.jpg")
colors = [(211, 158, 102), (22, 38, 58), (234, 206, 125), (47, 24, 20), (220, 62, 79), (205, 133, 150), (58, 20, 31),
          (133, 29, 37), (68, 103, 89), (237, 170, 156), (117, 93, 65), (45, 98, 138), (150, 69, 86), (221, 74, 62),
          (137, 164, 183), (26, 33, 32), (132, 34, 30), (82, 156, 118), (169, 147, 58), (237, 164, 171),
          (152, 176, 165), (77, 76, 34), (28, 85, 63), (45, 60, 88), (175, 202, 189), (102, 129, 158)]


xaxis = -320
yaxis = -310
my_turtle.teleport(xaxis, yaxis)


for dot_count in range(1, 101):
    my_turtle.dot(20, random.choice(colors))
    my_turtle.forward(70)

    if dot_count % 10 == 0:
        my_turtle.teleport(xaxis, yaxis+((dot_count//10)*70))

my_screen.exitonclick()
