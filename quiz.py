import string
import random
import datetime
import time

def intgenerator():
    x = random.randint(0, 6400)
    return x
chars = list(string.ascii_letters)
def chargenerator():
    a = random.randint(1, 5)
    if a == 5:
        x = str(random.randint(0,9))
    else:
        x = random.choice(chars)
    return x
def stringgenerator():
    x = ""
    a = random.randint(2,20)
    for i in range(a):
        b = random.randint(1,4)
        if b == 4:
            x += str(random.randint(0,9))
        else:
            x += random.choice(chars)
    return x
def floatgenerator():
    x = random.uniform(0.0, 9.99)
    x = round(x, 2)
    return x
def dategenerator():
    z = datetime.datetime(random.randint(2004, 2020), random.randint(1, 12), random.randint(1, 29))
    return z
def boolgenerator():
    possiblechar2 = ['a', 'b']
    a = random.choice(possiblechar2)
    b = random.choice(possiblechar2)
    if a == b:
        x = True
    else:
        x = False
    return x
lives = 3
score = 0
start = time.time()
while True:
    while True:
        question1 = intgenerator()
        print(f"Your score is {score} and you have {lives} lives left")
        print("Question 1 \n")
        print(question1)
        answer1 = input("What is this datatype:\nA : Integer\nB : Real/Float\nC : Boolean\nD : String\n")
        if answer1 == "A" or answer1 == 'a':
            score = score + 1
            print("Correct")
            break
        else:
            lives = lives - 1
            print("Incorrect")
            if lives == 0:
                break
    if lives == 0:
        print("You have lost all lives")
        break
    while True:
        question2 = stringgenerator()
        print(f"Your score is {score} and you have {lives} lives left")
        print("Question 2 \n")
        print(question2)
        answer2 = input("What is this datatype:\nA : Integer\nB : Real/Float\nC : Boolean\nD : String\n")
        if answer2 == "D" or answer2 == 'd':
            score = score + 1
            print("Correct")
            break
        else:
            lives = lives - 1
            print("Incorrect")
            if lives == 0:
                print("You have lost all 3lives")
                break
    if lives == 0:
        print("You have lost all lives")
        break
    while True:
        question3 = boolgenerator()
        print(f"Your score is {score} and you have {lives} lives left")
        print("Question 3 \n")
        print(question3)
        answer3 = input("What is this datatype:\nA : Integer\nB : Real/Float\nC : Boolean\nD : Char\n")
        if answer3 == "C" or answer3 == 'c':
            score = score + 1
            print("Correct")
            break
        else:
            lives = lives - 1
            print("Incorrect")
            if lives == 0:
                print("You have lost all 3lives")
                break
    if lives == 0:
        print("You have lost all lives")
        break
    while True:
        question4 = floatgenerator()
        print(f"Your score is {score} and you have {lives} lives left")
        print("Question4\n")
        print(question4)
        answer4 = input("What is this datatype:\nA : Integer\nB : Real/Float\nC : Boolean\nD : Char\n")
        if answer4 == "B" or answer4 == 'b':
            score = score + 1
            print("Correct")
            break
        else:
            lives = lives - 1
            print("Incorrect")
            if lives == 0:
                print("You have lost all 3lives")
                break
    break
end = time.time()
timetaken = round(end - start, 2)
if lives == 0:
    print(f"You scored {score} points before you died")
else:
    print(f"You took {timetaken} seconds. \nYou had {lives} lives left.")