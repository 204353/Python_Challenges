from random import choice
last2 = ['', '']
def newlast(x):
    last2[1] = last2[0]
    last2[0] = x
Artists = [['Queen'],[ "Guns'n'roses"], ["The Beatles"], ["Blink 182"], ["Green Day"], ["Drake"], ["Coldplay"], ["Obama"], ["Qadar"], ["Reuben"]]
songs = []
for i in range(1, 11):
    songs.append(i)
for i in range(0,10):
    Artists[i].append(songs)

i = 0
while i < 100:
    x = list(choice(Artists))
    y = choice(x[1])
    if x[0] not in last2:
        print(f"Band:{x[0]} Song:{y}")
        newlast(x[0])
        print(last2)
        i += 1