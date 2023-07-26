import turtle as t

import random

timmy = t.Turtle()
# random color
t.colormode(255)


# define the colour function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


# set the direction

timmy.speed("fastest")


def spirograph(size):
    for _ in range(int(360 / size)):
        timmy.color(random_color())
        timmy.circle(100)
        # to change the head because of spirograph
        timmy.setheading(timmy.heading() + size)


spirograph(5)

# tutle show long time
screen = t.Screen()
screen.exitonclick()
