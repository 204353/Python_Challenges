array = [1, 2, 3, 4, 5, 6, 7, 8]
while True:
    try:
        x = int(input("Enter a number that you want to find in a list:"))
        break
    except ValueError:
        print("Not a number")
def linearsearch(arr, x):
    for i in range(len(array)):
        if array[i] ==x:
            return i
    return -1
y = linearsearch(array,x)
if y >= 0:
    print("The number", x, "is found at index", y)
else:
    print("the number", x, "is not found in the list")