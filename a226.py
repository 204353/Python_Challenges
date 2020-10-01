def romanconverter (n):
    romannumeral = ''
    num = [4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  #we include 4 and 9 because in they have a different roman numeral
    romannum = ["MV̅", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV",  "I"]
    i = 0
    while n > 0:
        for b in range(n // num[i]):  #this is a floor division, which means that it rounds down
            romannumeral = romannumeral + romannum[i]
            n = n - num[i]
        i = i + 1
    return romannumeral
def intconverter(n):
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "v": 5000}  #this is a set because it uses these {}
    number = 0
    for i in range(len(n)):
        if i > 0 and num[n[i]] > num[n[i - 1]]:
            number = number + num[n[i]] - 2 * num[n[i - 1]]
        else:
            number = number + num[n[i]]
    return number

x = intconverter("Mv") #to designate 4000, we use a lower v as the proper symbol does not work.
y = romanconverter(4000)
print(x, y)