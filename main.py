from turtle import Turtle, Screen
import random

my_screen = Screen()
tim = []
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake")


def body(x):
    for i in range(0, x):
        tim.append(Turtle())
        tim[i].color("red")

def set_pos(x):
    jumper = 150
    for y in range(0, x):

        tim[y].penup()
        tim[y].goto(-230, jumper*-1)
        jumper -= 60

body(3)
set_pos(3)

my_screen.exitonclick()


