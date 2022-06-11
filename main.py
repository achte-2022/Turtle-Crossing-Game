import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# Object Setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.up, "Up")

manager = CarManager()

scoreboard = Scoreboard()
current_iteration = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_chance = random.randint(1, 7)
    if random_chance == 7:
        manager.create_new_car()
    manager.move_cars()
    if player.is_at_finish_line():
        player.new_level()
        scoreboard.update_score()
        manager.new_level()
    if manager.has_collided(player):
        game_is_on = False
        scoreboard.game_over()
    current_iteration += 1
screen.exitonclick()
