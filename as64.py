while True:
    try:
        x = input("Input a hex number")
        hexnumber = int(x, 16)
        print(hexnumber)
        print("Your hex number is", (hexnumber))
        break
    except ValueError:
        print("not a valid hex number")
print("Your ascii value is", chr(int(hexnumber)))