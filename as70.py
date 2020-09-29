import random
print("The objective of blackjack is to get to 21 using cards. Each card has a value.")
print("Cards 2-10 have a value of their number respectively. \nCards J, Q, and K have a value of 10.\nACE can have a value of 11 or 1. We'll decide which one to choose to make your life easier!")
possible_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'ACE']
player1cards = []
player2cards = []
player1cardvalue = 0
player2cardvalue = 0
for i in range(2):
    cardvalue = 0
    card = random.choice(possible_cards)
    player1cards.append(card)
    if type(card) == int:
        cardvalue = card
    elif type(card) == str:
        if card == 'ACE':
            if player1cardvalue <= 10:
                cardvalue = 11
            elif player1cardvalue > 10:
                cardvalue = 1
        else:
            cardvalue = 10
    player1cardvalue = player1cardvalue + cardvalue
for i in range(2):
    cardvalue = 0
    card = random.choice(possible_cards)
    player2cards.append(card)
    if type(card) == int:
        cardvalue = card
    elif type(card) == str:
        if card == 'ACE':
            if player2cardvalue <= 10:
                cardvalue = 11
            elif player2cardvalue > 10:
                cardvalue = 1
        else:
            cardvalue = 10
    player2cardvalue = player2cardvalue + cardvalue
#this part is to see ifanyone wants a new card
print(f"\nPlayer 1, your total is {player1cardvalue} as your cards are {player1cards}.\nPlayer 2, your total is {player2cardvalue} as your cards are {player2cards}")
while True:
    try:
        player1 = int(input("Press 1 if you want a new card. Press any other number if you don't.:"))
        if player1 == 1:
            cardvalue = 0
            card = random.choice(possible_cards)
            player1cards.append(card)
            if type(card) == int:
                cardvalue = card
            elif type(card) == str:
                if card == 'ACE':
                    if player1cardvalue <= 10:
                        cardvalue = 11
                    elif player1cardvalue > 10:
                        cardvalue = 1
                else:
                    cardvalue = 10
            player1cardvalue = player1cardvalue + cardvalue
            print(f"Your new total number is {player1cardvalue}, as your new card was {card} which has a value of {cardvalue}")
        else:
            break
    except ValueError:
        print("Not a number")
while True:
    try:
        player2 = int(input("\nPress 1 if you want a new card. Press any other number if you don't.:"))
        if player2 == 1:
            cardvalue = 0
            card = random.choice(possible_cards)
            player1cards.append(card)
            if type(card) == int:
                cardvalue = card
            elif type(card) == str:
                if card == 'ACE':
                    if player2cardvalue <= 10:
                        cardvalue = 11
                    elif player2cardvalue > 10:
                        cardvalue = 1
                else:
                    cardvalue = 10
            player2cardvalue = player2cardvalue + cardvalue
            print(f"Your new total number is {player2cardvalue}, as your new card was {card} which has a value of {cardvalue}")
        else:
            break
    except ValueError:
        print("Not a number")
#this determines who wins
if player1cardvalue ==21 :
    print("Player 1 wins")
elif player1cardvalue > 21:
    print('Player 1 disqualified therefore player 2 wins by default')
elif player2cardvalue == 21:
    print("player2 wins")
elif player2cardvalue > 21:
    print("Player 2 disqualified therefore player 1 wins by defualt")
elif player2cardvalue > 21 and player2cardvalue > 21:
    print("You both disqualified")
elif player1cardvalue == player2cardvalue:
    print("Yo it tied that's crazy")
elif player1cardvalue > player2cardvalue:
    print("player 1 wins")
elif player1cardvalue < player2cardvalue:
    print("player 2 wins")
else:
    print("something went wrong")

