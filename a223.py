array = []
neatnumbers = []
def findneatnumber(x):
    y = str(x)
    z = int(y[0]) + int(y[1]) + int(y[2])
    c = x/z
    c = str(c)
    if c[3] == '0':
        neatnumbers.append(x)
for i in range(101, 1000):
    array.append(i)
    findneatnumber(i)
print(*neatnumbers)