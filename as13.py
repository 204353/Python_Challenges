def gpmcalculator():
    gpm = gp/sales
    gpm = gpm*100
    print("Your gross profit margin was",gpm,"%")
def npmcalculator():
    npm = np/sales
    npm = npm*100
    print("Your net profit margin was",npm,"%")
while True:
    try:
        sales = float(input("Sales revenue:"))
        gp = float(input("Gross profit:"))
        if gp > sales:
            print("How can profit be higher than revenue? You must've gone wrong somewhere, try again!")
        else:
            break
    except ValueError:
        print("Error, not a number")
while True:
    try:
        np = float(input("Net profit:"))
        if np > sales:
            print("How can profit be higher than revenue? You must've gone wrong somewhere, try again!")
        else:
            break
    except ValueError:
        print("Error, not a number")
gpmcalculator()

npmcalculator()