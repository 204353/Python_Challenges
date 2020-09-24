import turtle
__import__("turtle").__traceable__ = False

jack = turtle.Turtle()
def drawsquare(t, sz):
    for i in ['black', 'white', 'green', 'cyan']:
        t.color(i)
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()
wn.bgcolor("indigo")
wn.title("Jack draws stuff")
size = 20
for i in range(10):
    drawsquare(jack, size)
    jack.color('indigo')
    jack.forward(size+50)
wn,mainloop()