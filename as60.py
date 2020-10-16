array = []
n = int(input("n"))
m = int(input("m"))
for i in range(0, n):
    if i == 0:
        string = ''
        string += '.'
        x = 0
        while x < len(string):
            if string[x] == '.':
                string += '*'
            else:
                string+='.'
            if len(string) == m:
                x += 2
            else:
                x += 1
        array.append(string)
    else:
        if m%2 == 1:
            x = array[-1][-1]
            if x == '*':
                string = ''
                string += '.'
                x = 0
                while x < len(string):
                    if string[x] == '.':
                        string += '*'
                    else:
                        string+='.'
                    if len(string) == m:
                        x += 2
                    else:
                        x += 1
                array.append(string)
            else:
                string = ''
                string += '*'
                x = 0
                while x < len(string):
                    if string[x] == '.':
                        string += '*'
                    else:
                        string+='.'
                    if len(string) == m:
                        x += 2
                    else:
                        x += 1
                array.append(string)
        else:
            x = array[-1][-1]
            if x == '*':
                string = ''
                string += '*'
                x = 0
                while x < len(string):
                    if string[x] == '.':
                        string += '*'
                    else:
                        string+='.'
                    if len(string) == m:
                        x += 2
                    else:
                        x += 1
                array.append(string)
            else:
                string = ''
                string += '.'
                x = 0
                while x < len(string):
                    if string[x] == '.':
                        string += '*'
                    else:
                        string+='.'
                    if len(string) == m:
                        x += 2
                    else:
                        x += 1
                array.append(string)
for i in range(len(array)):
    print(array[i])
