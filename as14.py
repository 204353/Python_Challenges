brackets = ["(", ")", "[", "]", "{", "}"]
bracketcount = 0
while True:
    try:
        string = input("Input a string")
        for char in string:
            if char in brackets:
                bracketcount = bracketcount + 1
        if bracketcount == 0:
            print("well there just aren't any brackets")
        else:
            bracketcount = bracketcount%2
            if bracketcount == 1:
                print("error:number of brackets are not equal")
            else:
                print("number of brackets are equal")
                break
    except ValueError:
        print("not a string")
