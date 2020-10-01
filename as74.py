def nandgate (a, b):
    z = 0
    if a == 0 or b == 0:
        z = 1
    return z

def orgate (a, b):
    a = nandgate(a, a)
    b = nandgate(b, b)
    z = nandgate(a, b)
    return z

def andgate (a, b):
    z = nandgate(a, b)
    z = nandgate(z, z)
    return z

def norgate (a, b):
    a = nandgate(a, a)
    b = nandgate(b, b)
    z = nandgate(a, b)
    z = nandgate(z, z)
    return z

def notgate (a):
    z = nandgate(a, a)
    return z

def xorgate (a, b):
    z = nandgate(a, b)
    a = nandgate(a, z)
    b = nandgate(b, z)
    z = nandgate(a, b)
    return z
while True:
    try:
        a = int(input("A : 1 or 0\n"))
        if a != 0 and a != 1:
            print("invalid")
        else:
            break
    except ValueError:
        print("invalid")

while True:
    try:
        b = int(input("B : 1 or 0\n"))
        if b != 0 and b != 1:
            print("invalid")
        else:
            break
    except ValueError:
        print("invalid")

print(f"nand is {nandgate(a, b)}")
print(f"or is {orgate(a, b)}")
print(f"and is {andgate(a, b)}")
print(f"nor is {norgate(a, b)}")
print(f"xor is {xorgate(a, b)}")
print(f"not is {notgate(a)} and {notgate(b)}")