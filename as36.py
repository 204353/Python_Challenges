numberlist = [1, 2, 3, 4, 5, 6, 7]
print("The first number is:", numberlist[0])
newlist = numberlist[::-1]
print("The last number is:", newlist[0])
newlist2 = []
newlist2.append(numberlist[0])
newlist2.append(newlist[0])
print(newlist2)
