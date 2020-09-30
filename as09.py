import random
list1 = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
likeness = 0
while True:
    y = random.choice(list1)
    print(y)
    a = input("Input:")
    if len(a) == len(y):
        a = a.lower()
        for i in range(len(y)):
            if a[i] == y[i]:
                likeness = likeness + 1
                print(f"The character {a[i]} was in both strings")
        print(f"Your likeness was{likeness}")
        break
    else:
        print("Not even the same length")