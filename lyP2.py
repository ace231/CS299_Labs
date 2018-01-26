# Alfredo Ceballos
# CS 299
# Project 3


import random


# Problem 1 #


# I made 2 different functions to handle calculating the BMI
# in either the metric or English/Imperial system
def bmi_met(w, h):
    bmi = float(w / (h * h))
    check_bmi(bmi)


def bmi_eng(w, h):
    bmi = float((w / (h * h)) * 703)
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


# This part of the program just runs a loop 12 times
i = 0
while i < 12:
    choice = input("Do you wish to check your BMI in the metric or English system? ").lower()
    try:
        if len(choice) == 0:
            print("No input detected, please try again...")
            continue
        elif choice == "exit" or choice == "stop":
            print("Goodbye...")
            break
        elif "english" in choice or choice[0] == 'e':
            weight = float(input("Enter your weight in pounds: "))
            height = int(input("Enter your height in inches: "))
            if weight == 0 or height == 0:
                print("Sorry, but 0 is not allowed as an input, try again.")
                continue
            bmi_eng(weight, height)
        elif "metric" in choice or choice[0] == 'm':
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            if weight == 0 or height == 0:
                print("Sorry, but 0 is not allowed as an input, try again.")
                continue
            bmi_met(weight, height)
        else:
            print("Your response was not recognized, please try again...")
        i = + 1
    except ValueError:
        print("The input provided was not valid, try again...")
    print("\n")
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


"""
Do you wish to check your BMI in the metric or English system? eng
Enter your weight in pounds: 150
Enter your height in inches: 70
Your BMI of 21.52 is normal

Do you wish to check your BMI in the metric or English system? eng
Enter your weight in pounds: 150
Enter your height in inches: 60
Your BMI of 29.29 signals you may be overweight

Do you wish to check your BMI in the metric or English system? e
Enter your weight in pounds: 150
Enter your height in inches: 55
Your BMI of 34.86 signals possible obesity

Do you wish to check your BMI in the metric or English system? eng
Enter your weight in pounds: 150
Enter your height in inches: 50
Your BMI of 42.18 signals possible extreme obesity

Do you wish to check your BMI in the metric or English system? met
Enter your weight in kilograms: 68.0389
Enter your height in meters: 1.778
Your BMI of 21.52 is normal

Do you wish to check your BMI in the metric or English system? met
Enter your weight in kilograms: 68.0389
Enter your height in meters: 1.524
Your BMI of 29.29 signals you may be overweight

Do you wish to check your BMI in the metric or English system? met
Enter your weight in kilograms: 68.0389
Enter your height in meters: 1.397
Your BMI of 34.86 signals possible obesity

Do you wish to check your BMI in the metric or English system? met
Enter your weight in kilograms: 68.0389
Enter your height in meters: 1.27
Your BMI of 42.18 signals possible extreme obesity

Do you wish to check your BMI in the metric or English system? 3/3/3
Your response was not recognized, please try again...

Do you wish to check your BMI in the metric or English system? fds
Your response was not recognized, please try again...

Do you wish to check your BMI in the metric or English system? 
No input detected, please try again...

Do you wish to check your BMI in the metric or English system? m
Enter your weight in kilograms: 
The input provided was not valid, try again...

Do you wish to check your BMI in the metric or English system? m
Enter your weight in kilograms: 0
Enter your height in meters: 0
Sorry, but 0 is not allowed as an input, try again.



Welcome to Paper, Rock, Scissors! Prepare to lose!
There will be 10 rounds. Ready? GO!
Please type either Paper, Rock, or Scissors: paper
You picked paper and the computer picked rock, you win!!!

Please type either Paper, Rock, or Scissors: rock
You picked rock and the computer picked scissors, you win!!!

Please type either Paper, Rock, or Scissors: rock
You picked rock and the computer picked paper, computer wins!!

Please type either Paper, Rock, or Scissors: rock
You and the computer both picked rock, it's a tie!!

Please type either Paper, Rock, or Scissors: scissors
You picked scissors and the computer picked paper, you win!!!

Please type either Paper, Rock, or Scissors: paper
You and the computer both picked paper, it's a tie!!

Please type either Paper, Rock, or Scissors: rock
You picked rock and the computer picked paper, computer wins!!

Please type either Paper, Rock, or Scissors: scissors
You picked scissors and the computer picked rock, computer wins!!

Please type either Paper, Rock, or Scissors: paper
You picked paper and the computer picked rock, you win!!!

Please type either Paper, Rock, or Scissors: rock
You picked rock and the computer picked scissors, you win!!!

You won 5 rounds out of 10!
"""
