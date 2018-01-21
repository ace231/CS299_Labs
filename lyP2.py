# Alfredo Ceballos
# CS 299
# Project 3


import random

# Problem 1 #

# I made 2 different functions to handle calculating the BMI
# in either the metric or English/Imperial system
def bmi_met(w, h):
    bmi = float(w / (h*h))
    check_bmi(bmi)

def bmi_eng(w, h):
    bmi = float((w / (h*h)) * 703)
    check_bmi(bmi)

# The calculated BMI from either function is checked here
def check_bmi(bmi):
    if bmi >= 40:
        print("Your BMI of %.2f signals possible extreme obesity" % bmi)
    elif bmi >= 30:
        print("Your BMI of %.2f signals possible obesity" % bmi)
    elif bmi >= 25:
        print("Your BMI of %.2f signals you may be overweight" % bmi)
    else:
        print("Your BMI of %.2f is normal" % bmi)

# This part of the program just runs a loop 12 times, unless the input from the
# user is not valid. In which case the counter, i, is not incremented
i = 0
while i < 12:
    choice = input("Do you wish to check your BMI in the metric or English system? ").lower()
    try:
        if choice == "exit" or choice == "stop":
            print("Goodbye...")
            break
        elif "english" in choice or choice[0] == 'e':
            weight = float(input("Enter your weight in pounds: "))
            height = int(input("Enter your height in inches: "))
            bmi_eng(weight, height)
            i += 1
        elif "metric" in choice or choice[0] == 'm':
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            bmi_met(weight, height)
            i += 1
        else:
            print("Your response was not recognized, please try again...")
    except ValueError:
        print("The input provided was not valid, try again...")
# End of problem 1


# Problem 2 #
# For the paper, rock, scissors game the computer is allowed to pick randomly
# from a list of 3 elements containing "paper", "rock", and "scissors".
# To pick randomly from the 3, the random module's choice function is used.
# The game loops 10 times and each time the computer's choice is checked
# against the players. All possibilities where the computer can win are checked 
# as well as the possibility the player and computer made the same choice.
# The last remaining possibility is where the player wins
print("\n\nWelcome to Paper, Rock, Scissors! Prepare to lose!")
print("There will be 10 rounds. Ready? GO!")
comp_choices = ["paper", "rock", "scissors"]
i = 0
player_wins = 0
while i < 10:
    comp_choice = random.choice(comp_choices)
    player_choice = input("Please type either Paper, Rock, or Scissors: ").lower()
    if comp_choice == player_choice:
        print("You and the computer both picked %s, it's a tie!!\n" % player_choice)
        i += 1
    elif player_choice == "rock" and comp_choice == "paper":
        print("You picked rock and the computer picked paper, computer wins!!\n")
        i += 1
    elif player_choice == "scissors" and comp_choice == "rock":
        print("You picked scissors and the computer picked rock, computer wins!!\n")
        i += 1
    elif player_choice == "paper" and comp_choice == "scissors":
        print("You picked paper and the computer picked scissors, computer wins!!\n")
        i += 1
    elif player_choice not in comp_choices:
        print("Your choice isn't valid! Try again!\n")
    else:
        print("You picked %s and the computer picked %s, you win!!!\n" % (player_choice, comp_choice))
        i += 1
        player_wins += 1
print("You won %d rounds out of 10!" % player_wins)

# End of problem 2



