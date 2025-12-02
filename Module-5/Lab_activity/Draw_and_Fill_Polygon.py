# Vrajkumar Patel
# 10/26/2025
# Program: Draws and fills a polygon based on user input

import turtle

def draw_polygon():
    # Setup turtle and screen
    screen = turtle.Screen()
    screen.setup(700, 700)
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(3)  # Not too fast, not too slow

    # Get input from user
    try:
        sides = int(input("How many sides? (3 or more): "))
        length = int(input("Length of each side: "))
        line_color = input("Line color: ").lower()
        fill_color = input("Fill color: ").lower()
    except ValueError:
        print("Oops! Please enter valid numbers.")
        return

    if sides < 3:
        print("A polygon needs at least 3 sides!")
        return

    # Angle calculation
    angle = 360 / sides

    # Set up turtle colors
    t.pencolor(line_color)
    t.fillcolor(fill_color)
    t.pensize(3)

    # Draw the polygon
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    t.end_fill()

    # Done Wait for user to close
    turtle.done()

# Run the function
draw_polygon()
