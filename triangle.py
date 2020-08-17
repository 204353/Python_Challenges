import turtle

def triangle_draw(x,y,sz) :
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range (3):
        turtle.forward(sz)
        turtle.right(120)
triangle_draw(0,0,120)