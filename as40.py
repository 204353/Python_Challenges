def clearscreen ():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
while True:
    try:
        print("Press 1 to clear the screen.")
        x = int(input(""))
        if x == 1:
            clearscreen()
            break
    except ValueError:
        print("not a number")
