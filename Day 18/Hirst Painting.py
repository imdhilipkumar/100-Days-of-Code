import random
import turtle as t
# object creation
timmy = t.Turtle()

colours = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
           (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
           (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
           (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# to choose the random color need to import the color mode
t.colormode(255)
# to speed up
timmy.speed("fastest")
# to remove the line
timmy.penup()
# to hide the turtle arrow
timmy.hideturtle()
# number of dots
num_dots = 100
# to make the angel in diagonal
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
for i in range(1, num_dots + 1):
    # dots
    timmy.dot(20, random.choice(colours))
    timmy.forward(50)
    # to cut 10* 10 like square

    if i % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)  # to end up into the starting line
        timmy.setheading(0)


# to remove the line


# screen
screen = t.Screen()
screen.exitonclick()
