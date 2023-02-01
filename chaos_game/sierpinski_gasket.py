import numpy as np
import turtle


def dot_in(t, coords):
    """
    Place a dot in the given coordinate.
    """
    # Draw the dot
    t.penup()
    t.goto(coords[0], coords[1])
    t.pendown()
    t.dot()


# Set up the screen
s = turtle.getscreen()
s.setup(width=1.0, height=1.0)

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # 0 is the fastest
turtle.hideturtle()
turtle.pen(pensize=1)


# Set three points for the triangle's vertices
height = 700
side = np.sqrt(4 * (height ** 2) / 3)
vertices = {'A': (0, height / 2), 
            'B': (side / 2, -height / 2), 
            'C': (-side / 2, -height / 2)}

# Draw the three vertices
dot_in(t, vertices['A'])
dot_in(t, vertices['B'])
dot_in(t, vertices['C'])
dot_in(t, (0, 0))  # Go home

# Start the game
turtle.pen(pensize=0.0001)
for iteration in range(500000):
    # Print the iteration number
    print(f"Current iteration: {iteration}")

    # Move halfway towards a vertex chosen at random
    rand_vertex = np.random.choice(['A', 'B', 'C'])
    new_pt = np.add(t.pos(), vertices[rand_vertex]) / 2
    dot_in(t, new_pt)

