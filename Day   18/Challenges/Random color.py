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
direction = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fast")
for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    # because of angle we use setheading
    timmy.setheading(random.choice(direction))
