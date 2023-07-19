from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_left():
    new_timmy = timmy.heading()+20
    timmy.setheading(new_timmy)


def move_right():
    new_timmy = timmy.heading()-20
    timmy.setheading(new_timmy)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forward, key="w")
screen.onkey(move_backward, key="s")
screen.onkey(move_left, key="a")
screen.onkey(move_right, key="d")
screen.onkey(clear, key="space")
screen.exitonclick()
