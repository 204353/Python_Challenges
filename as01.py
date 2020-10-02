mylist = [24,4,5,34,34,0]
for i in range(len(mylist)):
    for j in range(0, len(mylist) - i - 1):
        if mylist[j] >mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
print(*mylist)