import turtle
colors=['red', 'purple', 'blue', 'green',
        'yellow', 'orange', 'pink', 'gray', 'white']

turtle.bgcolor('black')
for x in range(360):
    turtle.pencolor(colors[x%9])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)
