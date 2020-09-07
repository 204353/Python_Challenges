while True:
    try:
        number = float(input("Enter a number and make sure it is a float!:"))
        print("wow nice number")
        break
    except ValueError:
        print("Error: Number is not a float")