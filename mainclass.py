from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-380, 0))
screen.listen()
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

right_paddle = Paddle((370, 0))
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
scoreboard = Score()
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(.02)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(right_paddle) < 40 and ball.xcor() > 350 or ball.distance(left_paddle) < 40 and ball.xcor() < -350:
        ball.bounce_pedal()

    if ball.xcor() > 380:
        ball.reset_position()
        right_paddle.clear()
        left_paddle.clear()
        right_paddle.goto((370, 0))
        left_paddle.goto((-380, 0))
        scoreboard.l_score()
    if ball.xcor() < -380:
        ball.reset_position()
        right_paddle.clear()
        left_paddle.clear()
        right_paddle.goto((370, 0))
        left_paddle.goto((-380, 0))
        scoreboard.r_score()

screen.exitonclick()
