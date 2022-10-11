from turtle import Turtle, Screen
import random

israceon = False
screen = Screen()
screen.setup(width=500, height=400)
userbet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green", "blue","purple"]
yposition = [-70, -40, -10, 20, 50, 80]
allturtles = []
for turt in range(0,6):
    newturtle = Turtle("turtle")
    newturtle.penup()
    newturtle.color(colors[turt])
    newturtle.goto(x=-230, y=yposition[turt])
    allturtles.append(newturtle)
if userbet:
    israceon = True

while  israceon:

    for turtle in allturtles:
        if turtle.xcor() > 230:
            israceon = False
            winningcolor = turtle.pencolor()
            if winningcolor == userbet:
                print(f"You've won! The {winningcolor} turtle is the winner")
            else:
                print(f"You've lost. The {winningcolor} turtle is the winner")
        randomwalk = random.randint(0,10)
        turtle.forward(randomwalk)





screen.exitonclick()