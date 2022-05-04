from turtle import Turtle


class Enemy(Turtle):
    def __init__(self, screenwidth, screenheight):
        super().__init__()
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.create_enemy()

    def create_enemy(self):
        self.direction = 1
        self.shape("./images/enemy.gif")
        self.penup()
        self.setheading(270)
        self.goto(0, self.screenheight / 2 - 100)

    def move_enemy(self):
        x, y = self.position()
        if self.direction == 1:
            self.goto(x + 0.05, y)
            if self.xcor() > self.screenwidth / 2 - 25:
                self.forward(10)
                self.direction = -1
        elif self.direction == -1:
            self.goto(x - 0.05, y)
            if self.xcor() < -self.screenwidth / 2 + 25:
                self.forward(10)
                self.direction = 1
