from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake_speed = 0.25

difficulty = screen.textinput(title="Choose Mode.", prompt=f"Welcome!\nChoose difficulty easy or hard.")

if difficulty.lower() == "hard":
    snake_speed = 0.1
else:
    snake_speed = 0.25

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake_speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.generate_food()
        snake.size_grow()
        scoreboard.change_score()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        snake.reset()
        scoreboard.reset_score()

    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            snake.reset()
            scoreboard.reset_score()

screen.exitonclick()
