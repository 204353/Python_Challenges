for i in range (1,21):
    number = i
    if number%3 == 0:
        x = "fizz"
    elif number%5 == 0:
        x = "buzz"
    elif number%3 == 0 and number%5 == 0:
        x = "fizzbuzz"
    else:
        x = i
    print(x)