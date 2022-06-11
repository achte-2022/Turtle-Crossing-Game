# Importing Libraries
from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_MAX = 250
Y_MIN = -250
X_INIT = 300
SHAPE = "square"
HEIGHT_FACTOR = 2
WIDTH_FACTOR = 1
LEFT = 180
COLLISION_DISTANCE = 20


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_increment = MOVE_INCREMENT
        self.move_distance = STARTING_MOVE_DISTANCE
        return

    def create_new_car(self):
        turtle_object = Turtle()
        turtle_object.penup()
        turtle_object.shape(SHAPE)
        color = random.choice(COLORS)
        turtle_object.color(color)
        turtle_object.shapesize(stretch_wid=WIDTH_FACTOR, stretch_len=HEIGHT_FACTOR)
        y = random.randint(Y_MIN, Y_MAX)
        turtle_object.goto(x=X_INIT, y=y)
        turtle_object.setheading(LEFT)
        self.car_list.append(turtle_object)
        return

    def move_cars(self):
        for cars in self.car_list:
            cars.forward(self.move_distance)
        return

    def new_level(self):
        self.move_distance += self.move_increment
        return

    def has_collided(self, player):
        for cars in self.car_list:
            if cars.distance(player) < COLLISION_DISTANCE:
                return True
        return False
