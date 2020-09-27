

while True:
    try:
        number = int(input("Input a number"))
        break
    except ValueError:
        print("Not a number")
bcdlist = []
for i in str(number):
    binary = int(i)
    binary = bin(binary)[2:]
    bcdlist.append(binary)
string = ""
print(f"the binary coded decimal for {number} is {string.join(bcdlist)}")
