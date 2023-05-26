from turtle import *

# Task 1


def draw_sun():
    hideturtle()
    bgcolor('sky blue')
    penup()
    goto(0, -150)
    pendown()
    color('yellow')
    begin_fill()
    circle(100)
    end_fill()


def draw_moon():
    hideturtle()
    bgcolor('black')
    color('white')
    begin_fill()
    circle(50)
    end_fill()
    penup()
    color('black')
    forward(20)
    pendown()
    begin_fill()
    circle(50)
    end_fill()


time_of_day = input("Введите время суток (день или ночь): ").lower()
speed(10000)
if time_of_day == "день":
    draw_sun()
elif time_of_day == "ночь":
    draw_moon()
else:
    print("Введено некорректное время суток. Введите 'день' или 'ночь'.")

exitonclick()


# Task 2
colors = ["pink", "orange", "yellow", "lime"]

radius = 50
line_width = 10

for color in colors:
    pensize(line_width)
    pencolor(color)
    circle(radius)

exitonclick()


# Task 3
pensize(15)
begin_fill()
fillcolor("light blue")

def plitka(b):
    for _ in range(b):
        for _ in range(3):
            forward(100)
            left(120)
        if b >= 2:
            forward(100)

plitka(4)
end_fill()
hideturtle()
exitonclick()
