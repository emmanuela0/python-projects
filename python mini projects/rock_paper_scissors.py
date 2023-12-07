import random

# Sets the user wins and computer wins to 0
user_wins = 0
computer_wins = 0

# Puts the valid choices in a list
choices = ["rock", "paper", "scissors"]

# Asks the user their choice in the game and converts it to lower case
#   if the user chooses "q", the game ends
#   if the user enters something invalid, a message is printed out and they
#       are prompted to enter a valid choice

while True:
    user_input = input("Type Rock, Paper, Scissors or Press Q to exit: ").lower()
    if user_input == "q":
        break

    if user_input not in choices:
        print("Your choice was not valid. Try again!")
        continue

# Generates a random number into a variable
    random_num = random.randint(0, 2)
    # rock: 0,  paper: 1, scissors: 2

# Computer choice is random and is shown to the user
    computer_choice = choices[random_num]
    print("Computer chose:", computer_choice)

# User input is compared to the computer choice
    if user_input == "rock" and computer_choice == "scissors":
            print("You won!")
            user_wins += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1

# Prints a message when there is a tie
    elif user_input == computer_choice:
        print("It's a tie! You win nothing.")

# Prints a message when the user loses
    else:
        print("You lost! What a shame... ")
        computer_wins += 1

# Outputs the amount of times the user and computer won
# Prints a goodby message
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Au revoir!")