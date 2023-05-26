from turtle import *

# Task 1
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
speed(100000)
# 1
t = Pen()
bgcolor('black')

for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)

# 2
up()
forward(1000)
down()
pensize(2)
for _ in range(72):
    for c in colors:
        color(c)
        circle(100)
        left(10)
hideturtle()
exitonclick()


# Task 2
penup()
goto(0,50)
pendown()
pensize(5)
color("light blue")
forward(50)
left(135)
forward(70)
left(135)
forward(50)
color("black")
pensize(2)
forward(30)
right(90)
forward(45)
left(135)
forward(50)
left(45)
forward(80)
left(45)
forward(50)
left(135)
forward(105)
exitonclick()
