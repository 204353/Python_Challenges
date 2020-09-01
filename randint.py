import random
numbers = []
for i in range (1,51):
    number = random.randint(1,1000)
    numbers.append(number)
print(numbers)
print("The Minimum number is", min(numbers))
print("The Maximum number is", max(numbers))
avg = sum(numbers)
avg = avg/50
print("The mean average is", avg)