# 100 Days of Code Capstone
# Space Invaders in Turtle

import random
import time
from turtle import Screen

from bullet import Bullet
from enemy import Enemy
from enemy_bullet import Enemy_Bullet
from player import Player
from scoreboard import Scoreboard

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 640
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
enemy_bullet = Enemy_Bullet(SCREEN_HEIGHT)
scoreboard = Scoreboard(SCREEN_WIDTH, SCREEN_HEIGHT)

screen.listen()
screen.onkeypress(player.player_left, "Left")
screen.onkeypress(player.player_right, "Right")
screen.onkeypress(fire_bullet, "space")

playing_game = True
while playing_game:
    # time.sleep(GAME_SPEED)
    screen.update()

    # Move bullets on screen
    bullet.move_bullets()
    enemy_bullet.move_bullets()

    # Move enemy
    enemy.move_enemy()

    # Create enemy bullet
    fire = time.localtime()
    if fire.tm_sec % 2 == 0:
        enemy_attack = random.choice(enemy.enemy_list)
        enemyx, enemyy = enemy_attack.position()
        enemy_bullet.create_bullet(enemyx, enemyy)

    # Check for bullet / enemy collision
    for bullet_check in bullet.bullet_list:
        for enemy_check in enemy.enemy_list:
            if bullet_check.distance(enemy_check) < 25:
                bullet_check.hideturtle()
                bullet.bullet_list.remove(bullet_check)
                enemy_check.hideturtle()
                enemy.enemy_list.remove(enemy_check)
                scoreboard.increase_score()

    # Check for enemy / player collision
    for enemy_check in enemy.enemy_list:
        if enemy_check.distance(player) < 50:
            scoreboard.game_over()
            playing_game = False

    # Check for enemy bullet / player collision
    for enemy_bullet_check in enemy_bullet.bullet_list:
        if enemy_bullet_check.distance(player) < 15:
            scoreboard.game_over()
            playing_game = False

    if enemy.enemy_list == []:
        scoreboard.game_win()
        playing_game = False

screen.exitonclick()
