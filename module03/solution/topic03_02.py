from turtle import *

# Task 1
pensize(2)
speed(50)
color("navy")
for l in range(4):
    for i in range(8):
        circle(i * 10)
    left(90)
hideturtle()
exitonclick()


# Task 2
pensize(2)
color('yellow')
speed(1000)
begin_fill()
for i in range(18):
    forward(150)
    left(100)
end_fill()
hideturtle()
exitonclick()


# Task 3
def draw_circle(color_name, position, fill):
    penup()
    goto(0, position)
    pendown()
    color(color_name)
    if fill:
        begin_fill()
    circle(35)
    if fill:
        end_fill()


draw_circle("red", 100, True)
draw_circle("yellow", 0, True)
draw_circle("green", -100, True)

hideturtle()
exitonclick()
