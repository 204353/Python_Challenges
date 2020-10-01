array = []
n = int(input("n"))
m = int(input("m"))
x = 0
for i in range(0, m):
    if x == 0: array.append(".")
    elif x == 1: array.append("*")
    if x == 0: x = 1
    elif x == 1: x = 0
for i in range(n):
    print(*array)