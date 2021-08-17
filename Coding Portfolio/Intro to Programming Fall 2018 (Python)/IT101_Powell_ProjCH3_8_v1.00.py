"""
Program: IT101_Powell_ProjCH3_8_v1.00.py
Due Date: 09/20/18
Author: Dustin Powell

--------------------------------------------------------------------------------
Objective: The program is to output the GCD of user inputed integers

--------------------------------------------------------------------------------
Project Algorithm:
1. Define what is needed to calcualte the GCD.
2. Prompt for user input of two integers.
3. Calcualte the inputs useing Euclid's algorithm.
4. Output the GCD of the two integers by using Euclid's algorithm.

--------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
--------------------------------------------------------------------------------
Acknowledgment Notes:
References come from the book and previous use of euclids algorithm in other
courses.

--------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of the program.
--------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_ProjCH3_8_v1.00.py
--------------------------------------------------------------------------------
Output:

-v1.00

Please enter the largest number: 40
Please enter the smallest number: 12
4 = 40 % 12
0 = 12 % 4
The GCD is:  4

--------------------------------------------------------------------------------
"""
#Libaries-----------------------------------------------------------------------
#NONE

#Global Constants---------------------------------------------------------------
#NONE

#Main Function Decleration------------------------------------------------------
def main():

    #Local Declerations-------------------------------------
    Large_Input = 0 #Stores the largest number inputed
    Small_Input = 0 #Stores the smallest number inputed
    remainder = 0   #Stores the remaidner of the two inputs

    #Local Statments----------------------------------------
    #Prompts user to input two intergers
    Large_Input = int(input("Please enter the largest number: "))
    Small_Input = int(input("Please enter the smallest number: "))

    #Loop to repeat the steps of Ecluid's Algorithm
    while True:
        
        #Calcualtes the remainder of the two inputs
        remainder = Large_Input % Small_Input
        
        #Prints the current remainder of the two inputs divided
        print(remainder, "=", Large_Input, "%", Small_Input)        
        
        #Defines the smallest input as the largest number to be divided
        Large_Input = Small_Input
        
        #If else statment to determine if remainder is equal to zero
        if remainder != 0:

            #If reamainder is not zero the remainder becomes the smallest input
            Small_Input = remainder
        else:

            #If the remainder is zero the loop stops because the GCD is found
            break

    #Outputs the calculated GCD of the two inputs.
    print("The GCD is: ", Small_Input)
    

#Function Declerations----------------------------------------------------------
#NONE

#Main Function Call-------------------------------------------------------------
main()
















