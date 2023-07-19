from turtle import Turtle, Screen
import random

# object creation
timmy = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# for Different angle
def shapes(nums_sides):
    for i in range(nums_sides):
        angle = 360 / nums_sides

        timmy.forward(100)
        timmy.right(angle)  # to mention of angle in specific shape


for shape in range(3, 11):
    timmy.color(random.choice(colours))
    shapes(shape)

screen = Screen()
screen.exitonclick()
