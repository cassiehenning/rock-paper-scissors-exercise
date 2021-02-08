import os 

USER_NAME = os.getenv("USER_NAME", default="Player One") 
print(f"PLAYER: '{USER_NAME}'")
#> "Player One"

print("Rock, Paper, Scissors, Shoot!")
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for an input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

#print(x)
#print("You chose: ", x)
print(f"You chose: {user_choice}")

#simulating a computer input

import random 

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")

if user_choice in options: 
    print("good")
else: 
    print("Please choose from either 'rock', 'paper', or 'scissors'")
#determining who won


#adapted from Kevin Pinkerton
wins = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
if (user_choice, computer_choice) in wins:
    print("You win!")
elif user_choice == computer_choice:
    print("You tied.")
else:
    print("You lose.") 

#print("-------------------")
#print("Oh, the computer won. It's ok.")
#print("-------------------")
print("Thanks for playing. Please play again!")