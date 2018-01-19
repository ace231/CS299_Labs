# Alfredo Ceballos
# CS 299
# Project 3


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
        print("Your BMI of %.2f signals possible overweightness" % bmi)
    else:
        print("Your BMI of %.2f is normal" % bmi)

# This part of the program just runs a loop 12 times, unless the input from the
# user is not valid. In which case the counter, i, is not incremented
i = 0
while i < 12:
    choice = input("Do you wish to check your BMI in the metric or English system? ")
    try:
        if choice == "exit" or choice == "stop":
            print("Goodbye...")
            break
        elif "english" in choice or choice[0] == 'e':
            weight = float(input("Enter your weight in pounds: "))
            height = int(input("Enter your height in inches: "))
            bmi_eng(weight, height)
            i = i + 1
        elif "metric" in choice or choice[0] == 'm':
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            bmi_met(weight, height)
            i = i + 1
        else:
            print("Your response was not recognized, please try again...")
    except ValueError:
        print("The input provided was not valid, try again...")
# End of problem 1


# Problem 2 #



# End of problem 2



