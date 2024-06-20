from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Partition
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((-390, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()
partition = Partition()


def exit_screen():
    screen.bye()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(exit_screen, "x")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ybounce()

    if ball.xcor() > 390:
        ball.change_turn()
        scoreboard.score_update("left")

    if ball.xcor() < -400:
        ball.change_turn()
        scoreboard.score_update("right")

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 360) or (ball.distance(l_paddle) < 50 and ball.xcor() < -370):
        print("bounce")
        ball.xbounce()
