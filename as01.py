thisarray = [1, 3, 4, 5, 3, 3, 5, 3, 4]
x = False

while x == False:
    x = True
    for i in range(0, len(thisarray)-1):
        if thisarray[i] > thisarray[i+1]:
            thisarray[i], thisarray[i+1] = thisarray[i+1],thisarray[i]
            x = False
print(thisarray)
