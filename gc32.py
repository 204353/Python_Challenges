import random
while True:
    choices = ["confess", "stay silent"]
    while True:
        try:
            userchoice = input("Do you choose to stay silent or confess:")
            if userchoice == "stay silent" or userchoice == "confess":
                break
            else:
                print("not a valid option, choose either 'confess' or 'stay silent'")
        except ValueError:
            print("error")
    computerchoice = random.choice(choices)
    print("the computer chose to", computerchoice)
    if userchoice == "confess" and computerchoice == "stay silent":
        print("You are free and the computer will serve 20 years!")
    elif userchoice == "stay silent" and computerchoice == "confess":
        print("The computer is free and you will serve 20 years!")
    elif userchoice == "stay silent" and computerchoice == "stay silent":
        print("you will both serve 1 year")
    elif userchoice == "confess" and computerchoice == "confess":
        print("you will serve 5 years")
    try:
        uc = int(input("press 1 to play again, press 2 to quit"))
        if uc == 2:
            break
    except ValueError:
        print("error")