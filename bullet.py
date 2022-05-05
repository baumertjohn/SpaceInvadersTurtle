from turtle import Turtle

BULLET_SPEED = 1


class Bullet(Turtle):
    def __init__(self, screenheight):
        super().__init__()
        self.hideturtle()
        self.screenheight = screenheight
        self.bullet_list = []

    def create_bullet(self, startx, starty):
        new_bullet = Turtle("circle")
        new_bullet.shapesize(0.5, 0.5)
        new_bullet.color("white")
        new_bullet.penup()
        new_bullet.setheading(90)
        new_bullet.goto(startx, starty + 50)
        self.bullet_list.append(new_bullet)

    def move_bullets(self):
        for count, bullet in enumerate(self.bullet_list):
            bullet.forward(BULLET_SPEED)
            if bullet.ycor() > self.screenheight / 2 + 20:
                bullet.hideturtle()
                del self.bullet_list[count]
