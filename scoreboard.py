from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.level_text()

    def level_text(self):
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", font=FONT)

    def level_increase(self):
        self.score += 1
        self.clear()
        self.level_text()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
