def make_it_laugh(string):
    vowels = ["a", "i", "o", "u", "e"]
    for i in string:
        if i in vowels:
            string = string.replace(i, "hahahahahahahahahahahaha")
    print(string)
string = input("Enter a word, and see the vowels get replaced by laughter:")
make_it_laugh(string)
