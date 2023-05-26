from turtle import *

# Task 1
pensize(2)
color('black')
speed(120)

for _ in range(4):
    forward(50)
    left(90)

penup()
goto(0, 50)
pendown()
left(60)
forward(50)
right(120)
forward(50)
exitonclick()


# Task 2
reset()
down()
color('red')
goto(50, 50)
setx(80)
sety(80)
write(position())
exitonclick()


# Task 3
pensize(5)
color('black')
left(90)
forward(150)
right(90)
forward(100)
right(90)
forward(150)
right(90)
forward(100)
penup()
pensize(2)
goto(0, 75)
pendown()
left(180)
forward(100)
penup()
goto(50, 0)
pendown()
left(90)
forward(150)
exitonclick()


# Task 4
def draw_filled_circle(x, y, radius, color_name):
    penup()
    goto(x, y)
    pendown()
    color(color_name)
    begin_fill()
    circle(radius)
    end_fill()
    penup()


pensize(2)
draw_filled_circle(0, 0, 60, "red")
draw_filled_circle(100, 100, 20, "blue")
draw_filled_circle(-100, 100, 40, "purple")
draw_filled_circle(-100, -100, 30, "violet")
draw_filled_circle(100, -100, 60, "yellow")

exitonclick()
