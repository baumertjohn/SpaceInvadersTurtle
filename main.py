# 100 Days of Code Capstone
# Space Invaders in Turtle

import time
from turtle import Screen

from bullet import Bullet
from enemy import Enemy
from player import Player

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GAME_SPEED = 0.1


def fire_bullet():
    startx, starty = player.position()
    bullet.create_bullet(startx, starty)


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.register_shape("./images/player.gif")
screen.register_shape("./images/enemy.gif")
screen.tracer(0)

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
bullet = Bullet(SCREEN_HEIGHT)

screen.listen()
screen.onkeypress(player.player_left, "Left")
screen.onkeypress(player.player_right, "Right")
screen.onkeypress(fire_bullet, "space")

playing_game = True
while playing_game:
    # time.sleep(GAME_SPEED)
    screen.update()

    # Move bullets up screen
    bullet.move_bullets()
    
    # Move enemy
    enemy.move_enemy()
    
    
    # Check for bullet / enemy collision    
    for bullet_check in bullet.bullet_list:
        if bullet_check.distance(enemy) < 25:
            print("HIT!!")
            bullet_check.hideturtle()
            bullet.bullet_list.remove(bullet_check)
            
        

screen.exitonclick()
