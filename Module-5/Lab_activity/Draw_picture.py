# Vrajkumar Patel
# 10/26/2025
# Program: Make a crazy colorful spinning star with turtle graphics

import turtle

def draw_rotating_star():
    screen = turtle.Screen()
    screen.bgcolor("black")  # Dark background = colors pop
    t = turtle.Turtle()
    t.speed(0)               # Fastest speed, no waiting
    t.pensize(2)

    colors = ["cyan", "magenta", "yellow", "white", "red", "lime"]
    segments = 150  # How many lines/loops

    for i in range(segments):
        t.pencolor(colors[i % len(colors)])  # Cycle colors
        t.forward(i * 2)                     # Longer line each time
        t.right(145)                         # Star twist
        t.circle(i / 5, 90)                  # Extra curve for fun

    t.hideturtle()  # Hide the turtle icon
    turtle.done()   # Keep window open

draw_rotating_star()
