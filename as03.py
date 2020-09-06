while True:
    try:
        str=input("input text:")
        mirror=str[len(str)::-1]
        print (mirror)
        toughdecision = input("do you want to go again,(yes or no)?:")
        if toughdecision == "no":
            break
    except ValueError:
        print("nope")