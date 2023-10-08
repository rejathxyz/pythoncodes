import turtle

# Set up the turtle screen
wn = turtle.Screen()
wn.bgcolor("white")

# Create a turtle object
tree = turtle.Turtle()
tree.color("green")
tree.width(2)

# Function to draw a fractal tree
def draw_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Set the starting position and angle
tree.left(90)
tree.up()
tree.backward(100)
tree.down()

# Call the function to draw the fractal tree
draw_tree(75, tree)

# Close the turtle graphics window on click
wn.exitonclick()