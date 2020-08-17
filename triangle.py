import turtle

def triangle_draw(x,y,sz) :
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range (3):
        turtle.forward(sz)
        turtle.right(120)
for x in range(-100,100,20):
    triangle_draw(x,100,120)
