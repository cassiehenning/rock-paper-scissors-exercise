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

#determining who won


#if UserChoice == ComputerChoice:
        print("It's tie!")
   elif UserChoice == "paper" and ComputerChoice == "rock":
        print("You win! Congrats")
    elif UserChoice == "paper" and ComputerChoice == "scissors":
        print("Oh! The computer won, that's ok!")
    elif UserChoice == "rock" and ComputerChoice == "paper":
        print("Oh! The computer won, that's ok!")
    elif UserChoice == "rock" and ComputerChoice == "scissors":
        print("You win! Congrats")
    elif UserChoice == "scissors" and ComputerChoice == "paper":
        print("You win! Congrats")
    elif UserChoice == "scissors" and ComputerChoice == "rock":
        print("Oh! The computer won, that's ok!")

print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")