import turtle

turtle.bgcolor("lightpink")
turtle.pensize(1.5)
turtle.speed(0.5)
color = ["red","blue", "orange", "green"]
for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)
        turtle.mainloop()