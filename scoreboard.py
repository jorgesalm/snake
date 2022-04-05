from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 265)
        self.write(f"Score: {self.score}", False, align="center",  font=("arial", 24, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("arial", 24, "normal"))