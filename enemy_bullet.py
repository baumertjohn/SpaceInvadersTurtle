from turtle import Turtle

BULLET_SPEED = 0.3
BULLET_COUNT = 4


class Enemy_Bullet(Turtle):
    def __init__(self, screenheight):
        super().__init__()
        self.hideturtle()
        self.screenheight = screenheight
        self.bullet_list = []

    def create_bullet(self, startx, starty):
        if not len(self.bullet_list) > BULLET_COUNT:
            new_bullet = Turtle("square")
            new_bullet.shapesize(0.125, 0.75)
            new_bullet.color("white")
            new_bullet.penup()
            new_bullet.setheading(270)
            new_bullet.goto(startx, starty)
            self.bullet_list.append(new_bullet)

    def move_bullets(self):
        for count, bullet in enumerate(self.bullet_list):
            bullet.forward(BULLET_SPEED)
            if bullet.ycor() < -self.screenheight / 2 - 20:
                bullet.hideturtle()
                del self.bullet_list[count]
