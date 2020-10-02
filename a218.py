trianglenumbers = []
letters = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1, 100001):
    x = i/2
    z = i + 1
    x = x*z
    trianglenumbers.append(x)

def triangleword(string):
    y = 0
    for i in string:
        x = letters.find(i)
        x += 1
        y += x
    return y
string = input()
y = triangleword(string.lower())
if y in trianglenumbers:
    print(f"The string has a value of {y}, which is the value of triangle number {trianglenumbers.index(y) + 1}")
else:
    print(f"the string has a value of {y}, which does not have the value of a triangle number")