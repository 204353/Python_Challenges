#top trump card game
import random

player1strength = random.randint(1, 100)
player2strength = random.randint(1,100)
player1speed = random.randint(1,100)
player2speed = random.randint(1,100)
player1utility = random.randint(1,100)
player2utility = random.randint(1,100)
player1hp = random.randint(1,100)
player2hp = random.randint(1,100)
print(f"Player 1: \nYour strength is {player1strength}.\nYour speed is {player1speed}.\nYour utility is {player1utility}.\nYour hp is {player1hp}")
print(f"Player 2: \nYour strength is {player2strength}.\nYour speed is {player2speed}.\nYour utility is {player2utility}.\nYour hp is {player2hp}")
while True:
    try:
        player1 = int(input("Player1\nPress 1 to use strength\nPress 2 to use speed\npress 3 to use utility \nPress 4 to use hp\n"))
        if player1 == 1:
            player1choice = player1strength
            player1decision = 'strength'
            print(f"You chose strength, which had a value of {player1strength}")
            break
        elif player1 == 2:
            player1choice = player1speed
            player1decision = 'speed'
            print(f"You chose speed, which had a value of {player1speed}")
            break
        elif player1 == 3:
            player1choice = player1utility
            player1decision = 'utility'
            print(f"You chose utility, which had a value of {player1utility}")
            break
        elif player1 == 4:
            player1choice = player1hp
            player1decision = 'hp'
            print(f"You chose hp, which had a value of {player1hp}")
            break
        else:
            print("Not a valid option")
    except ValueError:
        print("Not a number")
while True:
    try:
        player2 = int(input("Player2\nPress 1 to use strength\nPress 2 to use speed\npress 3 to use utility \nPress 4 to use hp\n"))
        if player2 == 1:
            player2choice = player2strength
            player2decision = 'strength'
            print(f"You chose strength, which had a value of {player2strength}")
            break
        elif player2 == 2:
            player2choice = player2speed
            print(f"You chose speed, which had a value of {player2speed}")
            player2decision = 'speed'
            break
        elif player2 == 3:
            player2choice = player2utility
            player2decision = 'utility'
            print(f"You chose utility, which had a value of {player2utility}")
            break
        elif player2 == 4:
            player2choice = player2hp
            player2decision = 'hp'
            print(f"You chose hp, which had a value of {player2hp}")
            break
        else:
            print("Not a valid option")
    except ValueError:
        print("Not a number")
if player1choice > player2choice:
    print(f"player 1 won as they chose {player1decision} which had a value of {player1choice}\nplayer2 chose {player2decision} which had a value of {player1choice}\nPlayer1's stat was higher!")
elif player1choice < player2choice:
    print(f"player 2 won as they chose {player2decision} which had a value of {player2choice}\nplayer1 chose {player1decision} which had a value of {player1choice}\nPlayer2's stat was higher!")
elif player1choice == player2choice:
    print(f"It was a tie as player1 chose {player1decision} which had a value of {player1choice}\nplayer2 chose {player2decision} which had a value of {player1choice}\nPlayer1 and Player2 had the same stat!")
else:
    print("somehow no-one won or tied")
