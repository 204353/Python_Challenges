english_to_morsecode = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '-':'-....-','':'',
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}

morsecode_to_english = {v:k for k,v in english_to_morsecode.items()}
def eng_to_m (message):
    translated = ''
    for i in message:
         translated += english_to_morsecode[i.upper()]
         translated += ' '
    print(translated)
def m_to_eng (message): 
    y = message.split(" ")
    translated = ''
    print(y)
    for i in y:
        if i == ' ':
            pass
        translated += morsecode_to_english[i]
    print(translated)

while True:
    try:
        print("1 : English to morsecode translator \n2 : morsecode to English translator \n3 : QUIT")
        x = int(input())
        if x == 1:
            message = input("Input your message in English:\n")
            eng_to_m(message)
        elif x == 2:
            message = input("Input your message in Morsecode. Use /  for spaces")
            m_to_eng(message)
        elif x == 3:
            break
        else:
            print("invalid, try again")
    except ValueError:
        print("Error, invalid option")
