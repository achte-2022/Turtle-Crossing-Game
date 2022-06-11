# Importing Libraries
from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SHAPE = "turtle"
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.new_level()
        self.move_distance = 10
        return

    def up(self):
        self.forward(self.move_distance)
        return

    def is_at_finish_line(self):
        return self.ycor() == FINISH_LINE_Y

    def new_level(self):
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        return
