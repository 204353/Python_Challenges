def Rövarspråket(string):
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    b = ""
    for i in string:
        b += i
        if i  in consonants:
            b += "o" + i
    print(b)

string = "bob"
Rövarspråket(string)