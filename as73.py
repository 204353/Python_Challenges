import random
choicelist = ["colour", "place", "pet"]
while True:
    try:
        print("What is your favourite", random.choice(choicelist))
        choice = input("")
        break
    except ValueError:
        print("Not a valid value")
n = random.randint(1, 20)
n = n + random.randint(1,100)
n = n + random.randint(1,1000)
firstnumber = n
n = n + random.randint(1,100)
n = n + random.randint(1,1000)
secondnumber = n
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = random.choice(alphabet)
y = random.choice(alphabet)
z = random.choice(alphabet)
a = random.choice(alphabet)
print("Your random password is", x+str(firstnumber)+y+choice+z+str(secondnumber)+a)