list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
clonedlist = list1[:]
print(clonedlist)
print(clonedlist is list1)
clonedlist [0] = 'A'
for char in list1:
    print(char)
for char in clonedlist:
    print(char)
for (i, v) in enumerate(list1):
    print(i, v)
bool1 = 'a' in list1
bool2 = 'a' in clonedlist
print(bool1, bool2)
del list1[0]
print(list1)
glue = ';'
list1 = glue.join(list1)
print(list1)