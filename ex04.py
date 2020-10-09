morsecode = {'A':'.-', 'B':'-...', 'C':'-.-.',
           'D':'-..', 'E':'.', 'F':'..-.',
           'G':'--.', 'H':'....', 'I':'..',
           'J':'.---', 'K':'-.-', 'L':'.-..',
           'M':'--', 'N':'-.', 'O':'---',
           'P':'.--.', 'Q':'--.-', 'R':'.-.',
           'S':'...', 'T':'-', 'U':'..-',
           'V':'...-', 'W':'.--', 'X':'-..-',
           'Y':'-.--', 'Z':'--..', ':':'---...',
           '1':'.----', '2':'..---', '3':'...--',
           '4':'....-', '5':'.....', '6':'-....',
           '7':'---...', '8':'---..', '9':'----.',
           '0':'-----', ' ':' ', '.':'.-.-.-',
           ',':'--..--', '?':'..--..', "'":".---.",
           '!':'-.-.--', '/':'-..-.', '(':'-.--.',
           ')':'-.--.-', '&':'.-...', ':': '---...',
           ';':'-.-.-.', '=':'-...-', '+':'.-.-.',
           '-': '-....-', '_':'..--.-', '"':'.-..-',
           '$':'...-..-', '@': '.--.-.'}
translator = {v: k for k, v in morsecode.items()} #this makes a reversed dictionary if it needs to be used for morse code
 #this converts the string to uppercase to reduce the length of the dictionary
translator = {v: k for k, v in morsecode.items()} #this makes a reversed dictionary if it needs to be used for morse code
def menu():
    print("Press 1 to convert text to morse")
    print("Press 2 to convert morse to text")
    print("Press 3 to end")
while True:
    try:
        menu()
        x = int(input())
        if x == 1:
            try:
                y = str(input("Input text:"))
                v = ''
                for i in y.upper():
                    v += morsecode[i]
                print(v)
            except KeyError:
                print("some part of that isn't text")
        elif x == 2:
            try:
                y = str(input("Input morse:"))
                v = ''
                for i in y.split():
                    v += translator[i]
                print(v)
            except KeyError:
                print("some part of that isn't morse")
        elif x == 3:
            break
        else:
            print('invalid')
    except ValueError:
        print('Value Error')
