def histogram( num ):
    for i in num:
        output = ''
        times = i
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([4, 9, 7])