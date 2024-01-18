#ROCK PAPER SCISSORS GAME

import random

options = ("Rock","Paper","Scissor")
running = True
user_score = 0
computer_score = 0
print("%%%%%%% ROCK PAPER SCISSOR GAME %%%%%%%")

while running:
    
    user_choice = None
    computer_choice = random.choice(options)

    while user_choice not in options:
        user_choice = input("Enter a choice between (Rock,Paper,Scisscor): ")
        
    print(f"User:{user_choice}")
    print(f"Computer:{computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "Rock" and computer_choice == "Scissor":
        print("User Wins!")
        user_score += 1
        
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("User Wins!")
        user_score += 1
        
    elif user_choice == "Scissor" and computer_choice == "Paper":
        print("User Wins!")
        user_score += 1
        
    else:
        print("Compter Wins!")
        computer_score += 1
        
    print(f"\nUser Score: {user_score} | Computer Score: {computer_score}")

        
    if not input("Play again?(yes/no):").lower() =="yes":
        running = False
        
print("Thanks for playing!Goodbye")
        
    