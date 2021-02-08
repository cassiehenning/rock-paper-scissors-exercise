print("Rock, Paper, Scissors, Shoot!")

import random 

print("-------------------")
print ("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print ("-------------------")

# asking user for an input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

#print(x)

#once it reaches the exit statement, it will stop running the code
#can be used to help fix errors

#print("you chose: ", x)

#string concat: 
#print("you chose: " + x)
#string interpolation / fofrmat string usage 
print(f"you chose: {user_choice}) 

# simulating a computer input 

options = ("rock", "Paper", "scissors") 
computer_choice = random.choice(foo)

print("you chose: "'rock,")
print("The computer chose: 'paper'")

exit()

# determining who won


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


#print("-------------------")
#print("Oh, the computer won. It's ok.")

#print("-------------------")
#print("thanks for playing. Please play again!")
