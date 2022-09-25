import turtle
def moving_object(move):
    move.fillcolor('orange')
    move.begin_fill()
    move.circle(20)
    move.end_fill()
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor('green')
screen.tracer(0)
move = turtle.Turtle()
move.color('orange')
move.speed(0)
move.width(2)
move.hideturtle()
move.penup()
move.goto(-250, 0)
move.pendown()
while True:
    move.clear()
    moving_object(move)
    screen.update()
    move.forward(0.5)