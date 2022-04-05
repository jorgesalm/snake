from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
snake = Snake()
food = Food()
score = Scoreboard()

game_on = True


my_screen.setup(height=600, width=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.listen()



while game_on:

    time.sleep(0.5)
    my_screen.update()
    snake.motion_body()
    my_screen.onkey(key="Left", fun=snake.left_motion)
    my_screen.onkey(key="Right", fun=snake.right_motion)
    my_screen.onkey(key="Up", fun=snake.up_motion)
    my_screen.onkey(key="Down", fun=snake.down_motion)

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        score.refresh()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -298 or snake.head.ycor() > 280 or snake.head.ycor() < -298:
        game_on = False
        score.game_over()

my_screen.exitonclick()