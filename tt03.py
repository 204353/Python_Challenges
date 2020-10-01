import turtle as t
def drawsquare(size, x , y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(8):
        t.forward(100)
        t.right(45)
drawsquare(4, 120 ,20)