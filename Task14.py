import turtle
n=int(input("Enter no of times you want to make turtle animation:"))
pen = turtle.Turtle()
for i in range(n):
    pen.forward(i * 10)
    pen.right(144)
turtle.done()