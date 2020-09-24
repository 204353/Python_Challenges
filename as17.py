while True:
    try:
        age = int(input("how old are you?:\n"))
        break
    except ValueError:
        print("isnt an age tbh")
if age < 17:
    print("You cannot drive and you cannot drink")
elif age >= 17 and age < 21:
    print("You can drive, but not drink")
else:
    print("you can drink and drive, just not at the same time")