def LEFT(string, length):
    string = string[0:length]
    return string
def RIGHT(string, length):
    string = string[-length::]
    return string
def MID(string, start, end):
    string = string[start-1:end-1]
    return string
def LENGTH(string):
    string = len(string)
    return string
def LCASE(string):
    newstring = ''
    for char in string:
        if char.islower():
            newstring += char
    return newstring
def UCASE(string):
    newstring = ''
    for char in string:
        if char.isupper():
            newstring += char
    return newstring
def To_Lower(string):
    string = string.lower()
    return string
def To_Upper(string):
    string = string.upper()
    return string
def Num_To_String(num):
    num = str(num)
    return num
def String_To_Num(string):
    string = float(string)
    return string
def INT(string):
    string = int(string)
    return string
def ASC(string):
    string = ord(string)
    return string
print("This is string manipulation")
while True:
    try:
        menu1 = int(input("Press 1 if you want to continue. Press 2 if you want to exit.\n"))
        if menu1 == 1:
            print("\nYou have chosen to continue.")
            while True:
                try:
                    menu2 = int(input("\nPress 1 to input a string.\nPress 2 to input a number\n"))
                    if menu2 == 1:
                        while True:
                            try:
                                string = input("enter a string")
                                break
                            except ValueError:
                                print("not a string")
                        while True:
                            try:
                                menu3 = int(input("\nPress 1 to use LEFT. \nPress 2 to use RIGHT. \nPress 3 to use MID. \nPress 4 to use LENGTH.\nPress 5 to use LCASE. \nPress 6 to use UCASE. \nPress 7 to use To_Lower. \nPress 8 to use To_Upper. \nPress 9 to use Num_To_String. \nPress 10 to use String_To_Num. \nPress 11 to use INT. \nPress 11 to use ASC.\n"))
                                if menu3 == 1:
                                    while True:
                                        try:
                                            length = int(input("Input your length\n"))
                                            break
                                        except ValueError:
                                            print("not a number")
                                    string = LEFT(string, length)
                                    print(string)
                                    break
                                elif menu3 == 2:
                                    while True:
                                        try:
                                            length = int(input("Input your length\n"))
                                            break
                                        except ValueError:
                                            print("not a number")
                                    string = RIGHT(string, length)
                                    print(string)
                                    break
                                elif menu3 == 3:
                                    while True:
                                        try:
                                            start = int(input("Enter your starting point\n"))
                                            end = int(input("Enter your end point\n"))
                                            break
                                        except ValueError:
                                            print("Not a number")
                                    string = MID(string, start, end)
                                    print(string)
                                    break
                                elif menu3 == 4:
                                    string = LENGTH(string)
                                    print(string)
                                    break
                                elif menu3 == 5:
                                    string = LCASE(string)
                                    print(string)
                                    break
                                elif menu3 == 6:
                                    string = UCASE(string)
                                    print(string)
                                    break
                                elif menu3 == 7:
                                    string = To_Lower(string)
                                    print(string)
                                    break
                                elif menu3 == 8:
                                    string = To_Upper(string)
                                    print(string)
                                    break
                                elif menu3 == 9:
                                    string = String_To_Num(string)
                                    print(string)
                                    break
                                elif menu3 == 10:
                                    string = INT(string)
                                    print(string)
                                    break
                                elif menu3 == 11:
                                    string = ASC(string)
                                    print(string)
                                    break
                                else:
                                    print("not an option")
                            except ValueError:
                                print("Not a number")
                        break
                    elif menu2 == 2:
                        while True:
                            try:
                                num = int(input("Enter your number to convert into a string"))
                                num = Num_To_String(num)
                                print(num)
                                break
                            except ValueError:
                                print("not a number")
                        break
                    else:
                        print("not an option")
                except ValueError:
                    print("Not a number")
        elif menu1 == 2:
            print("\nYou have chosen to exit.")
            break
        else:
            print("Not a valid option in the menu")
    except ValueError:
        print("That is not a number")