import turtle
def drawshape(x):
    for i in range(x):
        turtle.forward(40)
        turtle.right(360/x)
while True:
    try:
        x = int(input("input the number of sides"))
        if x < 3:
            print('cant be', x)
        else:
            break
    except ValueError:
        print("number")
drawshape(x)