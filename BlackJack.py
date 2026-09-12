logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random


def ace_or_eleven(current_deck):
    while sum(current_deck)>21 and 11 in current_deck:
        current_deck[current_deck.index(11)]=1
    return current_deck


def computers_game(current_deck):
    if sum(current_deck)<17:
        current_deck.append(random.choice(cards))
    return current_deck

def should_end_overall(user_deck, computer_deck):
    if sum(user_deck)>21:
        print(f"You lost, you went over 21\nYour Cards {user_deck}\nMy cards {computer_deck}")
        return False
    elif sum(computer_deck)>21:
        print(f"You win, I went over 21\nYour Cards {user_deck}\nMy cards {computer_deck}")
        return False
    elif sum(computer_deck) == 21:
        if sum(computer_deck) == sum(user_deck):
            print(f"Its a draw\nYour Cards {user_deck}\nMy cards {computer_deck}")
            return False
        else:
            print(f"I win by BLAckJAck\nYour Cards {user_deck}\nMy cards {computer_deck}")
            return False
    elif sum(user_deck) == 21:
        print(f"You win by BlackJAck\nYour Cards {user_deck}\nMy cards {computer_deck}")
        return False
    else:
        return True

def should_end_end(computer_deck,user_deck):
    if sum(computer_deck)<sum(user_deck):
        print(f"You win\nYour Cards {user_deck}\nMy cards {computer_deck}")
    elif sum(computer_deck)>sum(user_deck):
        print(f"You Lose\nYour Cards {user_deck}\nMy cards {computer_deck}")
    elif sum(computer_deck) == sum(user_deck):
        print(f"Its a draw\nYour Cards {user_deck}\nMy cards {computer_deck}")
    return False

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

play_blackjack=True
while play_blackjack:
    do_play = input("Do you want to play a game of BLackJack? Type 'yes' or 'no': ").lower()
    if do_play == "yes":
        computer_cards=[random.choice(cards),random.choice(cards)]
        computer_cards=ace_or_eleven(computer_cards)
        user_cards=[random.choice(cards),random.choice(cards)]
        user_cards=ace_or_eleven(user_cards)
        print("\n"*30)
        print(logo)
        print("Welcome to The BlackJack!\n")


        should_continue=True
        while should_continue:
            print(f'''Your cards: {user_cards}, current score: {sum(user_cards)}
                Computer's first card: {computer_cards[0]}
            ''')
            should_continue=should_end_overall(computer_deck=computer_cards,user_deck=user_cards)
            if should_continue:
                another_card=input("Type 'y' to get another card, type 'n' to pass: ")
                if another_card=='y':
                    user_cards.append(random.choice(cards))
                    user_cards=ace_or_eleven(user_cards)
                else:
                    while sum(computer_cards)<17:
                        computer_cards=computers_game(computer_cards)
                        computer_cards=ace_or_eleven(computer_cards)
                    should_continue=should_end_overall(user_deck=user_cards,computer_deck=computer_cards)
                    if should_continue:
                        should_continue=should_end_end(user_deck=user_cards, computer_deck=computer_cards)
    else:
        play_blackjack = False
