import random
n = []
c = n
for i in range(1, 112):
    n.append(i)
b = random.choice(n) #this is a constant please dont change this
i = 0
f = 0
print("We are thinking of a number from 1 to 111. Can you guess what it is? We'll tell you if it is higher or lower.")
while True:
    try:
        a = int(input("Input a number between 1 and 111\n"))
        e = n.index(a)
        f += 1
        if a > b:
            print(f"The number is lower than {a}.")
            del c[e::]
        elif a < b:
            print(f"The number is higher than {a}")
            del c[0:e+1]
        else:
            print(f"Wow you got it. It only took you {f} tries")
            break
    except ValueError:
        print("We already told you that that is not our number")
while True:
    a = random.choice(n)
    e = n.index(a)
    i += 1
    if a > b:
        del n[e::]
    elif a < b:
        del n[0:e+1]
    else:
        print(f"It took our cpu {i} tries to find our number.")
        break
