import random

floorschecked = []
while True:
    try:
        floors = int(input("No of floors\n"))
        if floors > 0:
            break
        else:
            print("Not a valid number of floors")
    except ValueError:
        print("Not a valid number of floors")

while len(floorschecked)< floors:
    securitychoice = random.randint(1, floors)
    if securitychoice not in floorschecked:
        print(f"\ncheck floor{securitychoice}")
        floorschecked.append(securitychoice)
        continue