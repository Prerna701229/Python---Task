import turtle
s = int(input("Enter the length of the side of the star: "))
col = input("Enter the color name or hex value of color(# RRGGBB): ")
t = turtle.Turtle()
t.fillcolor(col)
t.begin_fill()
for i in range(5):
    t.forward(s)
    t.right(144)
t.end_fill()