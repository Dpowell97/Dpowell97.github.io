"""
Program: IT101_Powell_ProjCH_5to7_Main_v1.00.py
Due Date: 10/11/18
Author: Dustin Powell

--------------------------------------------------------------------------------
Objective: Write a program that takes a bit string that can bit shift left or 
right and encrypts or decrypts the bit string

--------------------------------------------------------------------------------
Project Algorithm:
If encrypting bit string:
1. Prompt user for unencrypted string
2. Add one to each ASCII character value.
3. Convert to binary for shifting.
4. Shift the bit string to the left.
5. Output to user encrypted bit string.

If decrypting bit string:
1. Prompt user for encrypted bit string
2. Shift bit string to the right.
3. Convert to base 10.
4. Subtract one from the ASCII value.
5. Output the decryted bitstring.


--------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
--------------------------------------------------------------------------------
Acknowledgment Notes:
Some of the code snippets come from use in other coding projects in other 
classes.
The book was used for mutiple code snippets.


--------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of the program.
--------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_ProjCH_5to7_Main_v1.00.py
--------------------------------------------------------------------------------
Output:
-v1.00
Encryption / Decryption Program
-------------------------------
1. Encrypt a string
2. Decrypt a string
3. Exit Program


Please enter a integer for the selection: 1


Please enter a string to encrypt: hello
Encrypted message:  1010011 1001101 1011011 1011011 1100001

Please enter a integer for the selection: 2


Please enter the bit strings: 1010011 1001101 1011011 1011011 1100001
Decrypted message:  hello 

--------------------------------------------------------------------------------
"""
#Libraries-----------------------------------------------------------------------
#NONE


#Main Function Deceleration------------------------------------------------------
def main():

    #Local Declarations-------------------------------------

    selection = 0    #Stores the value of the user's selection
 
    #Local Statements----------------------------------------

    #While loop to determine user's operation
    while True:

        #Print statements to prompt user to make a selection
        print("Encryption / Decryption Program")
        print("-------------------------------")
        print("1. Encrypt a string")
        print("2. Decrypt a string")
        print("3. Exit Program")
        print("\n")
        
        #Stores user selection to variable selection
        selection = int(input("Please enter a integer for the selection: "))
        print("\n")

        #Nested if else statements to call functions to be performed
        if (selection == 1):

            #Calls function to encrypt a message
            _Encrypt_String_()

        else:
            if (selection == 2):
                 
                #Calls function to decrypt a bit string
                _Decrypt_String_()

            else:
                if (selection == 3):

                    #Breaks the while loop to end the program
                    break

                else:
                    
                    #Print statement to show user that a invalid selection was
                    # made.
                    print("The following is not a valid selection: "
                                  ,selection)
                    print("\n")
                        
#Function Declarations---------------------------------------------------------

#Function to shift bitstring to the left
def _Shift_Bit_String_Left_(user_Bitstring):

    #Local Declarations------------------------------------

    new_Bitstring = ""#String to store shifted bit string
    shiftNum = 0      #Stores the first value in bit string to prevent bit loss
    bitlength = 0     #Stores the largest index in the bit string

    #Local Statements--------------------------------------

    #Converts user_Bitstring to a list
    user_Bitstring = list(user_Bitstring)

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

        #Add each bit to the proper postion in the bit string
        new_Bitstring = new_Bitstring + str(user_Bitstring[i]) 
        
    #Returns to previous function
    return new_Bitstring

#Function to shift bitstring to the right
def _Shift_Bit_String_Right_(user_Bitstring):

    #Local Declerations------------------------------------

    shiftNum = 0      #Stores the last value in bit string to prevent bit loss
    bitlength = 0     #Stores the largest index in the bit string
    nNum = 0          #Stores the current index of bit that is to be shifted

    #Local Statments---------------------------------------

    #Converts user_Bitstring to a list
    user_Bitstring = list(user_Bitstring)

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

    #Returns to previous function
    return user_Bitstring

#Function to convert base 10 value to binary (Comes from book)
def _Convert_to_Binary_(decimal):

    #Local Declerations------------------------------------
    
    bitString = ""  #Stores the calcualted binary string.

    #Local Statments---------------------------------------

    #If statement to determine if the input is zero
    if decimal == 0:

        #Prints zero if input is zero
        print(0)

    else:

        #While loop to calculate base 10 number to binary
        while decimal > 0:

            #Calculates the remaidner of the base 10 number
            remainder = decimal % 2
            
            #Calculates the quotent of the base 10 number
            decimal = decimal // 2

            #Stores the binary number as a bit string.
            bitString = str(remainder) + bitString

    #Returns to previous function
    return bitString

#Function to convert bitstring to base 10 (Comes from book)
def _Convert_to_Decimal_(bitString):

    #Local Declerations------------------------------------

    decimal = 0  #Stores the calculated base 10 number

    #Local Statments---------------------------------------

    #Calculates the largest exponent needed for conversion
    exponent = len(bitString) - 1

    #For loop to calculate base 10 number
    for digit in bitString:
        
        #Calculates binary number to base 10
        decimal = decimal + int(digit) * 2 ** exponent

        #Decrements the exponent by one
        exponent = exponent - 1
   
    #Returns to previous function
    return decimal

#Function to encrypt a user inputed message
def _Encrypt_String_():

    #Local Declerations------------------------------------

    user_String = ""      #Stores the user inputed string
    charValue = 0         #Stores the ASCII character value
    encrptyed_String = "" #Stores the encrpyted string.
    
    #Local Statments---------------------------------------
    
    #Prompt user to input a string to encrpyt
    user_String = list(input("Please enter a string to encrypt: "))
    
    #For loop to encrypt use inputed string
    for i in range(len(user_String)):
    
        #Stores the ASCII value of a character
        charValue = ord(user_String[i])
        
        #Adds one to the ASCII value
        user_String[i] = charValue + 1
        
        #Function call to convert ASCII value to binary
        user_String[i] = _Convert_to_Binary_(user_String[i])
        
        #Function cal to shift bit string to the left
        user_String[i] = _Shift_Bit_String_Left_(user_String[i])

        #Statement to create string for output
        encrptyed_String = encrptyed_String + user_String[i] + " " 

    #Prints out encrypted bit strings from message
    print("Encrypted message: ", encrptyed_String, "\n\n")

#Function to decrypt a user inputed encrypted message
def _Decrypt_String_():

    #Local Declerations------------------------------------

    user_String = ""     #Stores the user input bit strings
    encrypted_String = ""#Stores the encrypted bit strings as list       
    decrypted_String = ""#Stores the decrypted message
    
    #Local Statments---------------------------------------

    #Prompts user to input bit strings
    user_String = input("Please enter the bit strings: ")

    #Method to remove spaces and store string as a list
    encrypted_String = user_String.split()

    #For loop to decrypt bit strings
    for i in range(len(encrypted_String)):

        #Function call to shift bit string to the right
        encrypted_String[i] = _Shift_Bit_String_Right_(encrypted_String[i])

        #Function call to convert bit string to binary
        decrypted_Char = _Convert_to_Decimal_(encrypted_String[i])

        #Subtracts one from the ASCII value
        decrypted_Char = decrypted_Char - 1

        #Converts ASCII value to a ASCII character
        decrypted_Char = chr(decrypted_Char)

        #Stores the new decrypted message in order        
        decrypted_String = decrypted_String + str(decrypted_Char)
    
    #Prints out user decryprted bit strings
    print("Decrypted message: ", decrypted_String, "\n\n")

#Main Function Call-------------------------------------------------------------
main()
















