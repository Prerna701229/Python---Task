import turtle
def colored_star():
    size = 80
    turtle.color("red")
    turtle.width(4)
    angle = 120
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
colored_star()