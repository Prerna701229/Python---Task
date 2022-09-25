import turtle
color=['red','purple','blue','orange','green','pink']
a=turtle.Pen()
turtle.bgcolor('black')
for i in range(500):
    a.pencolor(color[i%6])
    a.width(i/100+1)   
    a.forward(i)
    a.left(59)
turtle.done()
