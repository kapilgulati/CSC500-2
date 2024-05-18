"""
Author: Kapil Gulati
Date: 2024-05-17
Description: Python program to find the addition and subtraction of two numbers.
             The program will ask the user to input two numbers (num1 and num2) and perform
             addition (num1+num2) and subtraction (num1-num2) operation using the 2 numbers.
"""


# This function requests user to enter an Integer value, it expects message_for_input parameter
# The parameter value is displayed as message when asking for input
def get_input(message_for_input):
    # define boolean non-local variable with default value to True
    input_not_accepted = True  # we will use this variable to track if a valid value was entered
    # defne non-local variable with a default value of 0
    num_input = 0  # we will use this variable to store user input
    # the while loop will keep running until a valid value is provided
    while input_not_accepted:
        try:
            # read user input
            num_input = int(input(message_for_input))
        except:
            # if there is error in reading user input, then display message
            print("Invalid number, please try again.")
            # set value to True, so that while loop continue to run
            input_not_accepted = True
        else:
            # set value to False, so that while loop can terminate
            input_not_accepted = False
    # return value entered by the user
    return num_input


print("Given the two numbers, I will add and subtract number 1 and number 2")
num1 = get_input("Enter first whole number: ")
num2 = get_input("Enter second whole number: ")
print("Total after adding number 1 and number 2:", num1 + num2)
print("Total after subtracting number 2 from number 1:", num1 - num2)


