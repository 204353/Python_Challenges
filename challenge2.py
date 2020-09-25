import random
def LEFT(string, length):
    string = string[0:length]
    return string
def RIGHT(string, length):
    string = string[-length::]
    return string
def To_Upper(string):
    string = string.upper()
    return string
possiblestrings = ["Superman", "Batman","Clark Kent", "Bruce Wayne"]
score = 0
#Qeustion 1 test the LEFT function
while True:
    try:
        string = random.choice(possiblestrings)
        length = random.randint(1, 6)
        print(f"Question 1\nFor this function: \ndef Left(string, length):\n     string = string[0:length]\n     return string\nWhat will be printed when the string is {string} and the Length is {length}?:")
        question1 = input()
        string = LEFT(string, length)
        if question1 == string:
            score = score + 1
            print("\nSuccess!")
        else:
            print(f"\nIncorrect. The correct answer was '{string}'")
        break
    except ValueError:
        print("\nIncorrect Value")
#Question 2 tests the RIGHT function
while True:
    try:
        string = random.choice(possiblestrings)
        length = random.randint(1, 6)
        print(f"\nQuestion 2\nFor this function: \ndef RIGHT(string, length):\n     string = string[-length::]\n     return string\nWhat will be printed when the string is {string} and the Length is {length}?:")
        question2 = input()
        string = RIGHT(string, length)
        if question2 == string:
            score = score + 1
            print("\nSuccess!")
        else:
            print(f"\nIncorrect. The correct answer was '{string}'")
        break
    except ValueError:
        print("\nIncorrect Value")
#question3 tests the upper() function
while True:
    try:
        string = random.choice(possiblestrings)
        print(f"\nQuestion 3\nFor this function: \ndef To_Upper\n     string = string.upper()\n     return string\nWhat will be printed when the string is {string}?:")
        question3 = input()
        string = To_Upper(string)
        if question3 == string:
            score = score + 1
            print("\nSuccess!")
        else:
            print(f"\nIncorrect. The correct answer was '{string}'")
        break
    except ValueError:
        print("\nIncorrect Value")
print(f"You got {score}/3 which is {score/3 * 100}%")