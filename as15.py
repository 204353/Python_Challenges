def converter (km):
    print(km, "km is", round(km*0.62137119223733,3) ,"miles")

while True:
    try:
        km = float(input("enter a km value that you would like to be converted to miles:"))
        converter(km)
        break
    except ValueError:
        print("Just isn't a number")