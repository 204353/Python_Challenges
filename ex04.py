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
    translator = {v: k for k, v in morsecode.items()} #this translates the user input into morse code 1 by 1
    if '-' in txt or '.' in txt:
        return ''.join(translator[i] for i in txt.split())#this looks to make sure if
    return ' '.join(morsecode[i] for i in txt.upper())
while True:
    try:
        menu = int(input("Type 1 if you wish to use the translator, or type 2 if you want to exit the program:"))
        if (menu == 1):
            inputs = input("Input what you would like to be converted. For morse code, please use spaces to designate between a letter\n:")
            print(morse(inputs))
            break
        elif (menu ==2):
            break
    except ValueError:
        print("Error: Please go again")
