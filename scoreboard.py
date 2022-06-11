# Importing Libraries
from turtle import Turtle

# Constants
FONT = ("Courier", 24, "normal")
X_INIT = -280
Y_INIT = 260
ALIGN = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=X_INIT, y=Y_INIT)
        self.score = 1
        self.draw_scoreboard()
        return

    def draw_scoreboard(self):
        score_text = f"Level: {self.score}"
        self.write(score_text, align=ALIGN, font=FONT)
        return

    def update_score(self):
        self.clear()
        self.score += 1
        self.draw_scoreboard()
        return

    def game_over(self):
        self.goto(x=-83, y=0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
        return
