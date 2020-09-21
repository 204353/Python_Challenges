likeness = 0
def likefinder(likeness):
    for char in string1:
        if char in string2:
            likeness = likeness + 1
    return likeness
string1 = "monday"
while True:
    print("The string is", string1)
    string2 = input("input your string:")
    n = likefinder()
    print(n)
    if int(n) < len(string1):
        print("Hack unsuccessful")
    else:
        print("Hack successful")
        break
