from turtle import Turtle, Screen, distance
import random

screen = Screen()
w = 1000
h = 800
screen.setup(w, h)

colors = ["red", "yellow", "blue", "magenta", "green", "black"]

user_bet = screen.textinput(title="racing bet", prompt="make you bet in color: ")
turtles = []

game_is_on = True


def create_turtle(color_string):
    t = Turtle(shape="turtle")
    t.color(color_string)
    t.shapesize(3, 3)
    return t


for color in colors:
    turtle = create_turtle(color)
    turtles.append(turtle)


for turtle in turtles:
    turtle.penup()
    turtle.goto(-w/2 + 20, -h/3+60*turtles.index(turtle))

if user_bet:
    game_is_on = True

while game_is_on:
    for turtle in turtles:
        if turtle.position()[0] >= w/2 - 30:
            game_is_on = False
            if turtle.fillcolor() == user_bet:
                print("You win")
            else:
                print("you lose")
        distance = random.randint(0, 30)
        turtle.forward(distance)


screen.exitonclick()
