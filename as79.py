def makeitlaugh(word):
    vowels = ["a", "i", "o", "u", "e"]
    for i in word:
        if i in vowels:
            word = word.replace(i, "hahahahahahahahahahahaha")
    print(word)
word = input("Enter a word, and see the vowels get replaced by laughter:")
makeitlaugh(word)