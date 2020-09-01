while True:
    try:
        isbn = int(input("Enter your isbn :"))
        if len(str(isbn)) == 10:
            digit1 = int(repr(isbn)[0]) * 10
            digit2 = int(repr(isbn)[1]) * 9
            digit3 = int(repr(isbn)[2]) * 8
            digit4 = int(repr(isbn)[3]) * 7
            digit5 = int(repr(isbn)[4]) * 6
            digit6 = int(repr(isbn)[5]) * 5
            digit7 = int(repr(isbn)[6]) * 4
            digit8 = int(repr(isbn)[7]) * 3
            digit9 = int(repr(isbn)[8]) * 2
            cd = int(repr(isbn)[9])
            total = digit1 + digit2 + digit3 + digit4 + digit5 + digit6 + digit7 + digit8 + digit9
            total = total%11
            total = 11- total
            if cd == total:
                print("Correct")
                break
            else:
                print("incorrect ")
        else:
            print("Invalid length")
    except ValueError:
        print("not a number")