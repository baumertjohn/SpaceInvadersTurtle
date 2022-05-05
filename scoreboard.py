from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self, screenwidth, screenheight):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, self.screenheight / 2 - 35)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 30, "bold"))

    def game_win(self):
        self.goto(0, 0)
        self.write(f"YOU WIN", align="center", font=("Arial", 30, "bold"))
