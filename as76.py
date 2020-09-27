array = [18,5,6,7,192,1]
array = sorted(array)
print(array)
x = 200*200*200*200
for i in range(len(array)-1):
    if array[i+1] - array[i] < x:
        x = array[i+1] - array[i]
print(x)