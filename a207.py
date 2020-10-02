list1 = []
while True:
    try:
        x = int(input("How many words will you input?"))
        for i in range(x):
            y = input("input the word")
            list1.append(y)
        break
    except ValueError:
        print("error")
print(f"The sorted list is:{sorted(list1)}")
file = open('savedfile.txt', 'w')
file.write(str(sorted(list1)))
file.close()