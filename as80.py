import math
def area(radius):
    area = round(math.pi * radius * radius, 1)
    return area
def circumference(radius):
    circumference = round(2 * math.pi * radius, 1)
    return circumference
while True:
    try:
        radius = float(input("Please enter the radius of your circle:\n"))
        print(f"The area of your cirlce is {area(radius)} and the circumference of your circle is {circumference(radius)}")
        break
    except ValueError:
        print("Not a valid radius")
