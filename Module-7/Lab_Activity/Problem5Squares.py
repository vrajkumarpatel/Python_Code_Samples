# Your Name: Vrajkumar Patel
# The Date: 2025-11-10
# Problem 5: Squares
# Description: Use the provided base chunk (not shown here) to produce the desired image.
# pattern of rotated squares using the turtle module. Adjust counts, angles, and sizes


import turtle


def draw_square(t: turtle.Turtle, size: int) -> None:
    """Draw a single square of a given size."""
    for _ in range(4):
        t.forward(size)
        t.right(90)


def main():
    screen = turtle.Screen()
    screen.title("Problem 5: Squares")

    t = turtle.Turtle()
    t.speed(0)  # fastest drawing
    t.width(2)

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # Draw a set of rotated squares that grow in size
    size = 20
    rotations = 36  # number of squares to draw
    growth = 8      # how much each square grows in size
    angle = 10      # rotation between squares

    for i in range(rotations):
        t.color(colors[i % len(colors)])
        draw_square(t, size + i * growth)
        t.right(angle)

    # Keep the window open until the user closes it
    turtle.done()


if __name__ == "__main__":
    main()