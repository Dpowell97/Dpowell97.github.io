"""
Program: IT101_Powell_Ch4Proj_5_ShiftL_v1.py
Due Date: 10/11/18
Author: Dustin Powell

--------------------------------------------------------------------------------
Objective: Write a program the shifts bit string to the left

--------------------------------------------------------------------------------
Program Algorithm:
1. Recieve user inputed bit string
2. Shift the bitstring to the left.
3. Output shifted bitstring.

--------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
--------------------------------------------------------------------------------
Acknowledgment Notes:
Course book was used for syntax

--------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of the program.
--------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_Ch4Proj_5_ShiftL_v1.py
--------------------------------------------------------------------------------
Output:
-v1.00
Please enter a bit string: 10010
Starting bit string : ['1', '0', '0', '1', '0']


Left shift bit string:  ['0', '0', '1', '0', '1']


--------------------------------------------------------------------------------
"""
#Libaries-----------------------------------------------------------------------
#NONE

#Main Function Decleration------------------------------------------------------
def _Shift_Bit_String_Left_():

    #Local Declerations-------------------------------------

    user_Bitstring = "" #Stores the user inputed bit string
    bitlength = 0     #Stores the largest index in the bit string

    #Local Statments----------------------------------------
    
    #Prompts user to input a bit string
    user_Bitstring = list(input("Please enter a bit string: "))

    #Prints the user inputed bitstring before changes
    print("Starting bit string :", user_Bitstring)
    print("\n")
    
    #Determines the last index value of user_Bitstring
    bitlength = len(user_Bitstring) - 1
    
    #For loop to shift bit string to the left
    for i in range(len(user_Bitstring)):

        #Nested if else statments to shift bits
        if(i == 0):

            #Stores first bit to avoid bit loss
            shiftNum = user_Bitstring[i]

            #Shifts right bit to the left
            user_Bitstring[i] = user_Bitstring[i+1]
        else:

            #If statement to determine end of bit string
            if(i == bitlength):
                
                #Inserts bit at end of bit string
                user_Bitstring[i] = shiftNum

            else:

                #Shifts a bit to the left
                user_Bitstring[i] = user_Bitstring[i+1]
                 
    #Prints the shifted bit string to screen
    print("Left shift bit string: ", user_Bitstring)
    print("\n")

#Function Declerations----------------------------------------------------------
#NONE

#Main Function Call-------------------------------------------------------------
_Shift_Bit_String_Left_()





