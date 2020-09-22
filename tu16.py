myvar = 129.0
print(f"RM{myvar}")


numcol1 = [3, 6, 8]
numcol2 = [2, 5, 7]
numcol3 = [1, 4, 6]

print("\Table 1")
for i in range(3):
    print(f"{numcol1[i]:<15} {numcol2[i]:<15} {numcol3[i]:<15}")

print("\nTable 2")
for i in range(3):
    print(f"{numcol1[i]:>15.2f} {numcol2[i]:>15.2f} {numcol3[i]:>15.2f}")
# Note the order here. >15 and then .2f which is 2 decimal places

print("\nTable 3")
for i in range(3):
    print(f"{numcol1[i]:^15.2f} {numcol2[i]:^15.2f} {numcol3[i]:^15.2f}")

while True:
    try:
        number = int(input("\nInput any positive integer"))
        if number < 0:
            print("error")
        else:
            print(f"\nBinary is :{number:b}")
            break
    except ValueError:
        print("\nnot an integer")