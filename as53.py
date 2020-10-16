voters = [[["Alice"],["Bob"],["Charlie"]],
    [["Alice"],["Charlie"],["Bob"]],
    [["Bob"],["Charlie"],["Alice"]],
    [["Bob"], ["Alice"], ["Charlie"]],
    [["Charlie"], ["Bob"], ["Alice"]]]
a = 0 #votes for alice
b = 0 #votes for bob
c = 0 #votes for charlie
for i in voters:
        if 'Charlie' in i[0]:
            c += 1
        elif 'Alice' in i[0]:
            a += 1
        elif 'Bob' in i[0]:
            b += 1
totalvotes = a+b+c
while True:
    if a/totalvotes >= 0.50:
        break
        print("Alice wins")
    elif b/totalvotes >= 0.50:
        print("Bob wins")
        break
    elif c/totalvotes >= 0.50:
        print("Charlie wins")
        break
    else:
        if c == min(a, b, c):
            print('s')
            for i in voters:
                if 'Charlie' in i[0]:
                    if 'Alice' in i[1]:
                        a += 1
                    else:
                        b += 1
        elif b == min(a, b, c):
            print('s')
            for i in voters:
                if 'Bob' in i[0]:
                    if 'Alice' in i[1]:
                        a += 1
                    else:
                        c += 1
        elif a == min(a, b, c):
            print('s')
            for i in voters:
                if 'Alice' in i[0]:
                    if 'Charlie' in i[1]:
                        c += 1
                    else:
                        b += 1