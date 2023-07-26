from turtle import Turtle, Screen
import random
# object creation
is_race_on = False
screen = Screen()
# to get the turtle frame
screen.setup(width=500, height=400)
# get the user input
user_bet = screen.textinput(title=" Make your Bet ", prompt=" Which Turtle will the race , Enter the color : ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
# position of y
y_position = [-70, -40, -10, 20, 50, 80]
# to create the empty list to store all turtle
all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
# to hind the line
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
# to get to the corner of the frame
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


# to start the race
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtle:
        # for the speed
        # winning state
        if turtle.xcor() > 230:
            # to stop the race
            is_race_on = False
            winning_turtle = (turtle.pencolor())
            if user_bet == winning_turtle:
                print(f"You've  WON , the {winning_turtle} is the WINNER ...!!!")
            else:
                print(f"You've  LOST , the {winning_turtle} is the WINNER ...!!!")

        random_dist = random.randint(1, 10)
        turtle.forward(random_dist)
screen.exitonclick()
