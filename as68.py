import random
Colours = ["R", "G", "B", "Y"]
def RandomCard():
    colour = random.choice(Colours)
    number = random.randint(1, 9)
    Card = colour + str(number)
    return Card
pcard = []
ccard = []
for i in range(0, 7):
    pcard.append(RandomCard())
    ccard.append(RandomCard())
thiscard = 'B1'
while True:
    while True:
        a = len(pcard) + 1
        for i in ccard:
            cplay = RandomCard()
            ccard.append(cplay)
            x = ccard[-1]
            if x[1] == thiscard[1] or x[0] == thiscard[0]:
                cplay = x
                break
        print(f"The CPU chose to play {cplay}")
        print(ccard)
        print(f"Your cards are {pcard}")
        card_played = int(input("Which card will you play(The first card is 1, the second is 2, etc...\nIf you do not have any cards to play, press 0\n"))
        if card_played == 0:
            print("You chose to pick a new card")
            while True:
                newcard = RandomCard()
                pcard.append(newcard)
                print(f"The CPU chose to play {cplay}")
                print(f"The new card you recieved was {newcard}")
                decision = int(input("Are you satisfied with this card? Press 1 if yes and you choose this card.\nPress any other number if no and you want another card\n"))
                if decision == 1:
                    played_card = newcard
                    pcard.remove(newcard)
                    break
                else:
                    print("You chose to pick a new card")
            break
        elif card_played <= a:
            card_played = card_played - 1
            played_card = pcard[card_played]
            pcard.remove(played_card)
            break
        elif card_played > len(pcard):
            print("not possible")
        else:
            print("Not possible")
    print(f"You chose to play {played_card}")
    print(f"The CPU chose {cplay}")
    if played_card[0] == cplay[0] or played_card [1] == cplay[1]:
        print("You can Continue as the card you played has a matching feature with the card the CPU played")
        thiscard = played_card
    else:
        print("Tough luck, but the card you played had no matching features with the card the CPU played, and you didn't choose another card.\nI guess you lose")
        break
    if len(pcard) == 0:
        print("YOU WIN!")
        break
    elif len(ccard) == 0:
        print("The CPU WINS")
        break
