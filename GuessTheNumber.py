logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
import random
def game():
    chosen_number=random.randint(1,100)
    print(logo)
    print(f"Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty=='easy':
        chances=10
    else:
        chances=5
    while chances>0:
        print(f"You have {chances} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        if guess>chosen_number:
                print("Too High")
        elif guess<chosen_number:
                print("Too Low")
        else:
                print(f"You got it! The answer was {chosen_number}.")
                return None
        chances-=1
        if chances>0:
            print("Guess again.")

        else:
            print("You've run out of guesses, you lose.")
            print(f"The number was {chosen_number}.")
game()
