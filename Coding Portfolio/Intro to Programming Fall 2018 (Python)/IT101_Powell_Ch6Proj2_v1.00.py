"""
Program: IT101_Powell_Ch6Proj2_v1.00.py 
Due Date: 11/1/18
Author: Dustin Powell

-------------------------------------------------------------------------------
Objective: Write a program that uses a recursive function of Newton's method
to approximate a square root of a user inputted number.

-------------------------------------------------------------------------------
Project Algorithm:
1. Receive user inputted value.
2. Call a function to compute the approximation of the inputted number.
3. Repeat the function until the approximation of the inputted number is found.
4. When the approximate value is found output to screen.

-------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
-------------------------------------------------------------------------------
Acknowledgment Notes:
The book was used for the code snippet of Newton's Method.
The use of try and except comes from the online python documentation:
https://docs.python.org/3/tutorial/errors.html
Worked with Peyton Whitefield to find issues with recursion in code.

-------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of program

-------------------------------------------------------------------------------
Compiler Used:

python3 IT101_Powell_Ch6Proj2_v1.00.py
-------------------------------------------------------------------------------
Output:

Square Root Approximation Program
---------------------------------

Please enter a positive number: 4
The approximation of square root 4.0 is 2.0

-------------------------------------------------------------------------------
"""

#Libraries---------------------------------------------------------------------
import math

#Main Function Declaration-----------------------------------------------------
def main():

    #Local Declarations------------------------------------
    user_Input = 0.0   #Stores user's inputted number
    aprox_Num = 1.0     #Stores the approximation to be evaluated
    calculated_Aprox = 0.0  #Stores the calculated approximated square root

    #Local Statements--------------------------------------

    #Stores the program header for program print out
    print("Square Root Approximation Program")
    print("---------------------------------\n")

    #While loop to handle errors if an appropriate value is not inputted
    while True:

        #Try statement to test if an error occurs
        try:
           
           #Input statement to receive number to find approximate square root
           user_Input = float(input("Please enter a positive number: "))

           #Absolute value statement to prevent negative numbers from being
           # calculated.
           user_Input = abs(user_Input)

           #Terminates the while loop
           break

        #Except statement to handle errors that occur from incorrect values
        # being inputted
        except (TypeError, ValueError):

           #Print statement to prompt the user to input correct values
           print("Please enter a valid value")

    #Function call to calculate the approximate square root of a number    
    calculated_Aprox = _Newton_Method_(user_Input, aprox_Num)

    #Prints the user inputted number and the calculated approximation
    print("The approximation of square root", user_Input, "is", calculated_Aprox)
   
    
#Function Declarations---------------------------------------------------------

#Function to calculate the approximate square root of a number
def _Newton_Method_(user_Input, aprox_Num):

    #Local Declarations------------------------------------
    old_Aprox = 0.0 #Stores the old approximation value

    #Local Statements--------------------------------------

    #Declares the current approximation value to old_Aprox
    old_Aprox = aprox_Num

    #Evaluates the current approximation of the square root
    aprox_Num = float((aprox_Num + user_Input / aprox_Num) / 2)

    #If statement to determine if the approximate value has been found
    if old_Aprox == aprox_Num:

        #Returns the approximated number to function call
        return aprox_Num

    #Function call to evaluate the approximation again
    aprox_Num = _Newton_Method_(user_Input, aprox_Num)

    #Returns the approximated number to function call
    return aprox_Num


#Main Function Call------------------------------------------------------------
main()

