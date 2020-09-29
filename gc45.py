while True:
    try:
        char = input("Input 1 character")
        if len(char) == 1:
            print("Good job")
            break
        else:
            print("No")
    except ValueError:
        print("not a character")
