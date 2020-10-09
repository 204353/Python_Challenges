import random
n = []
for i in range(1, 112):
    n.append(i)
i = 0
while True:
    x = random.choice(n)
    print(x)
    e = n.index(x)
    a = input()
    a = a.lower()
    if a == 'higher':
        del n[0:e+1]
        i += 1
    elif a == 'lower':
        del n[e::]
        i += 1
    else:
        print(f"It took {i} tries")
        break
