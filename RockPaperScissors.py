rps=['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
import random
computer_choice=random.choice(['r','p','s'])
print("Welcome to Rock Paper Scissors!")
player_choice=input("What do you choose? Rock(R), Paper(P) or Scissors(S): ").lower()
print("You chose-")
if player_choice=='r':
    print(rps[0])
elif player_choice=='p':
    print(rps[1])
else:
    print(rps[2])
print("I choose-")
if computer_choice=='r':
    print(rps[0])
elif computer_choice=='p':
    print(rps[1])
else:
    print(rps[2])
if computer_choice==player_choice:
    print("It's a Draw...")
elif computer_choice=='r':
    if player_choice=='s':
        print("You lose!!")
    if player_choice=='p':
        print("You win :)")
elif computer_choice=='s':
    if player_choice=='r':
        print("You win XD")
    if player_choice=='p':
        print("You Lose :(")
elif computer_choice=='p':
    if player_choice=='r':
        print("LOSER!")
    if player_choice=='s':
        print("YOU WON!")
