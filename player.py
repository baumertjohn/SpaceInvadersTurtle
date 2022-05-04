from turtle import Turtle

MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self, screenwidth, screenheight):
        super().__init__()
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.create_player()

    def create_player(self):
        self.clear()
        self.shape("./images/player.gif")
        self.penup()
        self.setheading(90)
        self.goto(0, -self.screenheight / 2 + 40)

    def player_left(self):
        x, y = self.position()
        if x > -self.screenwidth / 2 + 20:
            self.goto(x - MOVE_DISTANCE, y)

    def player_right(self):
        x, y = self.position()
        if x < self.screenwidth / 2 - 20:
            self.goto(x + MOVE_DISTANCE, y)
