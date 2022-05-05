from turtle import Turtle

ENEMY_SPEED = 0.2  # 0.2 works well


class Enemy(Turtle):
    def __init__(self, screenwidth, screenheight):
        super().__init__()
        self.hideturtle()
        self.direction = 1
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.enemy_list = []
        self.start_game()

    def create_enemy(self, x, y):
        new_enemy = Turtle("./images/enemy.gif")
        new_enemy.penup()
        new_enemy.setheading(270)
        new_enemy.goto(x, self.screenheight / 2 - y)
        self.enemy_list.append(new_enemy)

    def start_game(self):
        for y in range(
            int(self.screenheight / 2 - 100), int(self.screenheight / 2 - 226), -50
        ):
            for x in range(-225, 226, 75):
                self.create_enemy(x, y)

    def move_enemy(self):
        for enemy in self.enemy_list:
            x, y = enemy.position()
            if self.direction == 1:
                enemy.goto(x + ENEMY_SPEED, y)
                if enemy.xcor() > self.screenwidth / 2 - 25:
                    for enemy in self.enemy_list:
                        enemy.forward(10)
                    self.direction = -1
            elif self.direction == -1:
                enemy.goto(x - ENEMY_SPEED, y)
                if enemy.xcor() < -self.screenwidth / 2 + 25:
                    for enemy in self.enemy_list:
                        enemy.forward(10)
                    self.direction = 1
