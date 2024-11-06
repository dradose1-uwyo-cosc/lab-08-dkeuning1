# Daniel Keuning
# UWYO COSC 1010
# 11/5/2024
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
#   - Used openstax to find copy and paste the quadratic formula
#   - Used ChatGPT to check if the solutions were correct

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def check(string):
    if string == int or string == float:
        return True
    else:
        try:
            string = round(float(string), 2)
            return True
        except:
            return False

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False



print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list


def slope_formula(slope, intercept, x_upper, x_lower):
    list = []

    while x_lower <= x_upper:
        y = slope * x_lower + intercept
        x_lower += 1
        list.append(y)
    
    return(list)

while True:
    print("Type 'exit' to quit.")
    slope = (input("Enter slope. "))
    if slope == "exit":
        break
    intercept = (input("Enter Y-intercept. "))
    if intercept == 'exit':
        break
    x_lower = (input("Lower x bound: "))
    if x_lower == 'exit':
        break
    x_upper = (input("Upper x bound: "))
    if x_upper == 'exit':
        break
    if is_float(x_lower) is False or is_float(x_upper) is False:
        print("ERROR: Please enter valid numbers.")
    elif check(slope) is False or check(intercept) is False:
        print("ERROR. Please enter valid numbers.")
    elif x_lower > x_upper:
        print("ERROR. Please try again.")
    else:
        break
try:
    slope = float(slope)
    intercept = float(intercept)
    x_lower = int(float(x_lower))
    x_upper = int(float(x_upper))

    if x_lower > x_upper:
        print("ERROR. Lower bound cannot be higher than upper bound.")

    print(f"Answers: {slope_formula(slope, intercept, x_upper, x_lower)}")

except ValueError:
    print("ERROR. Please try again.")


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math

def quadratic_formula (a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Null"
    else:
        x1 = round((-b+math.sqrt(b**2-4*a*c))/(2*a), 2)
        x2 = round((-b-math.sqrt(b**2 - 4*a*c))/(2*a), 2)
        return x1, x2

while True:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = int(input("Enter C: "))
    break


answer = quadratic_formula(a, b, c)

print(f"Solutions: {answer}")
