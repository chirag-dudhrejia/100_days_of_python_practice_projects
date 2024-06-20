import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.forward_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()
    if cars.collision(player):
        game_is_on = False
        scoreboard.game_over()

    if player.ycor() > 250:
        scoreboard.next_level()
        player.goto_starting_line()
        cars.lvl_up()


screen.exitonclick()