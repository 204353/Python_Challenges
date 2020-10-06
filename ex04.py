def morse(txt):
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
               '7':'---...', '8':'---..', '9':'----.', '0':'-----', ' ':' '}
    translator = {v: k for k, v in morsecode.items()} #this makes a reversed dictionary if it needs to be used for morse code
    if '-' in txt or '.' in txt: #this checks whether the input is morse code or letters
        return ''.join(translator[i] for i in txt.split())#this will split up the morse code into a list
    return ' '.join(morsecode[i] for i in txt.upper()) #this converts the string to uppercase to reduce the length of the dictionary
while True:
    try:
        menu = int(input("Type 1 if you wish to use the translator, or type 2 if you want to exit the program:"))
        if (menu == 1):
            inputs = input("Input what you would like to be converted.\n:")
            print(morse(inputs))
            break
        elif (menu ==2):
            break
    except ValueError:
        print("Error: Please go again")
