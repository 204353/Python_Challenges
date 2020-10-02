letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encoder(string, shift):
    newstring = ''
    for i in string:
        if i == 'Z':
            x = letters[shift]
            x += 1
            newstring += letters[x]
        else:
            x = letters.find(i)
            x += shift
            newstring += letters[x]
    return newstring
def decoder(string, shift):
    newstring = ''
    for i in string:
        if i == 'Z':
            x = letters[shift]
            x -= 1
            newstring += letters[x]
        else:
            x = letters.find(i)
            x -= shift
            newstring += letters[x]
    return newstring
while True:
    try:
        question = int(input("Press 1 for Encoder\nPress 2 for Decoder\n"))
        if question != 1 and question != 2:
            print("Not an option")
        else:
            string = input("Input your string of letters\n")
            shift = int(input("Input the shift\n"))
            if question == 1:
                a = encoder(string, shift)
                print(f"Your cipher is {a, b}")
            elif question == 2:
                b = decoder(string, shift)
                print(f"The original string was {b}")
            break
    except ValueError:
        print("not a number")