list1 = ["Netherlands"]
while True:
    try:
        print(f"The list is {list1}\nThe last letter in the list currently is {list1[-1]}")
        nextone = input("Input a string that starts with the last letter of the last string in the list")
        lastone = list1[-1]
        lastletter = str(lastone)
        lastletter = lastletter[-1]
        if nextone in list1:
            print("It can't be in the list")
            break
        else:
            if nextone[0].lower() == lastletter:
                list1.append(nextone)
                print("congrats")
            else:
                print("You failed")
                break
    except ValueError:
        print("Value Error")
