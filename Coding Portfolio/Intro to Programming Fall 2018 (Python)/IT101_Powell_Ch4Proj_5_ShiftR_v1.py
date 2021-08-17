"""
Program: IT101_Powell_ProjCH2_4_v1.py
Due Date: 10/11/18
Author: Dustin Powell

--------------------------------------------------------------------------------
Objective: Write a program the shifts bitstring to the left

--------------------------------------------------------------------------------
Program Algorithm:
1. Recieve user inputed bit string
2. Shift the bit string to the right.
3. Output shifted bit string.

--------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
--------------------------------------------------------------------------------
Acknowledgment Notes:
Course book used for syntax

--------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of the program.
--------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_Ch4Proj_5_ShiftR_v1.py
--------------------------------------------------------------------------------
Output:
-v1.00
Please enter a bit string: 10010
Starting bit string:  ['1', '0', '0', '1', '0']


Right shift bit string:  ['0', '1', '0', '0', '1']

    

--------------------------------------------------------------------------------
"""
#Libaries-----------------------------------------------------------------------
#NONE


#Main Function Decleration------------------------------------------------------
def _Shift_Bit_String_Right_():

    #Local Declerations-------------------------------------

    user_Bitstring = ""#Stores user inputed bit string
    bitlength = 0      #Stores the largest index in the bit string
    nNum = 0           #Stores the current index of bit that is to be shifted
    shiftNum = 0       #Stores the last value in bit string to prevent bit loss

    #Local Statments----------------------------------------

    #Prompts user to input a bit string
    user_Bitstring = list(input("Please enter a bit string: "))
    
    #Outputs current bit string state
    print("Starting bit string: ",user_Bitstring)
    print("\n")
    
    #Calculates the length of the user_Bitstring
    bitlength = len(user_Bitstring) - 1
    
    #For loop to shift bit string to the right
    for i in range(len(user_Bitstring)):
        
        #Calculates the distance from the last index to i
        nNum = bitlength - i
        
        #Nested if else statements to shift bits
        if(nNum == bitlength):

            #Stores the last bit to prevent bit loss
            shiftNum = user_Bitstring[nNum]

            #Shifts a bit to the right by one
            user_Bitstring[nNum] = user_Bitstring[nNum-1]


        else:
            if(nNum == 0):

                #Inserts a bit at index 0 to finsih the bit shift.
                user_Bitstring[nNum] = shiftNum
            else:
          
                #Shifts a bit to the right
                user_Bitstring[nNum] = user_Bitstring[nNum-1]

    #Outputs the shifted bit string
    print("Right shift bit string: ", user_Bitstring)
    print("\n")
    

#Function Declerations----------------------------------------------------------
#NONE

#Main Function Call-------------------------------------------------------------
_Shift_Bit_String_Right_()
















