from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def go_forward():
    t.forward(10)

def go_backward():
    t.backward(10)

def turn_ccw():
    t.left(10)

def turn_cw():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(fun=go_forward, key="w")
screen.onkey(fun=go_backward, key="s")
screen.onkey(fun=turn_ccw, key="a")
screen.onkey(fun=turn_cw, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
