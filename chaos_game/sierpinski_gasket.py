import numpy as np
import turtle


def dot_in(t, x, y):
    """
    Place a dot in the given coordinate.
    """
    # Draw the dot
    t.penup()
    t.goto(x, y)
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
pt_a = (0, height / 2)  
pt_b = (side / 2, -height / 2)  
pt_c = (-side / 2, -height / 2) 

# Draw the three vertices
dot_in(t, pt_a[0], pt_a[1])
dot_in(t, pt_b[0], pt_b[1])
dot_in(t, pt_c[0], pt_c[1])
dot_in(t, 0, 0)  # Go home

# Start the game
turtle.pen(pensize=0.0001)
for iteration in range(500000):
    # Print the iteration number
    print(f"Current iteration: {iteration}")

    # Throw the die
    die_roll = np.random.randint(1, 7)

    # Move halfway towards A when we get 1 or 2 
    if die_roll in [1, 2]:
        new_pt = np.add(t.pos(), np.subtract(pt_a, t.pos()) / 2)
        dot_in(t, new_pt[0], new_pt[1])

    # Move halfway towards B when we get 3 or 4
    elif die_roll in [3, 4]:
        new_pt = np.add(t.pos(), np.subtract(pt_b, t.pos()) / 2)
        dot_in(t, new_pt[0], new_pt[1])

    # Move halfway towards C when we get 5 or 6
    elif die_roll in [5, 6]:
        new_pt = np.add(t.pos(), np.subtract(pt_c, t.pos()) / 2)
        dot_in(t, new_pt[0], new_pt[1])
