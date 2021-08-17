"""
Program: IT101_Powell_Stats_Ch5Proj1_v1.00.py
Due Date: 10/25/18
Author: Dustin Powell

-------------------------------------------------------------------------------
Objective: Write a program that outputs the mean, median, and mode of a set of
values

-------------------------------------------------------------------------------
Program Algorithm:
1. Receive user inputted set of numbers
2. Send set of numbers to function to find the mean
3. Calculate the mean
4. Return to main function to print the mean
5. Send set of numbers to a function to find the median
6. Calculate the median
7. Return to main function to print the median
8. Send set of numbers to function to find the mode(s)
9. Calculate the mode(s)
10. Return to main function to print the mode(s)

-------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
-------------------------------------------------------------------------------
Acknowledgment Notes:
Course book used for syntax, chapter 5 code snippets, and some methods.
In class instruction for formula and ways to calculate mean, median, and mode.
Used to following links to for list of methods for list and dictionaries:
https://www.programiz.com/python-programming/methods/dictionary
https://www.programiz.com/python-programming/methods/list
Worked with Peyton Whitefield to solve problems with code.

-------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of the program.
-------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_Stats_Ch5Proj1_v1.00.py
-------------------------------------------------------------------------------
Output:
-v1.00
Enter a list of num: 1 2 3 4 5 6 7 7 8 9
The mean is 5.2
The median is 5.5
The mode(s) of the set: 7.0 

-------------------------------------------------------------------------------
"""
#Libraries---------------------------------------------------------------------
#NONE

#Main Function Declaration-----------------------------------------------------
def main():

    #Local Declarations------------------------------------
    calculated_mean = 0   #Stores the calculated mean
    calculated_median = 0 #Stores the calculated median  
    calculated_mode = 0   #Stores the calculated mode
    extra_mode = 0        #Stores a copy of the mode to prevent duplicates

    #Local Statements--------------------------------------
    
    #Prompt user to input a set of numbers
    list_of_Nums = input("Enter a number or set of numbers: ")

    #String method to remove spaces and turn string into a list
    list_of_Nums = list_of_Nums.split()

    #Function call to calculate the mean and stores the result
    calculated_mean = _Find_Mean_(list_of_Nums)

    #Print function to output calculated mean
    print("The mean is", calculated_mean)
    
    #Function call to calculate the median and stores the result
    calculated_median = _Find_Median_(list_of_Nums)

    #Print function to output calculated median
    print("The median is", calculated_median)

    #Function call to calculate the mode and stores the result
    calculated_mode = _Find_Mode_(list_of_Nums)

    #If else statement if a mode exist or not
    if calculated_mode != 0:
        
        #Print statement for header of mode output
        print("The mode(s) of the set:", end = " ")

        #For loop to prevent duplicate modes from printing
        for i in range(len(calculated_mode)):
            
            #If else statement to start determine if a element is a duplicate
            if i != 0:
                
                #If statement to only print values that have not been outputted
                if extra_mode != calculated_mode[i]:
                    
                    #Declares current mode to extra_mode to be compared
                    extra_mode = calculated_mode[i]
                    
                    #Prints the mode of the set
                    print(calculated_mode[i], end = " ")

            else:
                
                #Declares current mode to extra_mode to be compared
                extra_mode = calculated_mode[i]
                
                #Prints the mode of the set
                print(calculated_mode[i], end = " ")

        #Used to create spacing after output of mode
        print("\n")

    else:
        
        #Prints the mode of the set
        print("The mode(s) of the set:", calculated_mode)

        #Used to create spacing after output of mode
        print("\n")

    
    

#Function Declarations---------------------------------------------------------

#Function to calculate the mean of a set of numbers
def _Find_Mean_(list_of_Nums):

    #Local Declarations------------------------------------
    mean = 0        #Stores the calculated mean
    sum_of_Nums = 0 #Stores the sum of the numbers in the set

    #Local Statements--------------------------------------

    #For loop to calculate the sum of the list of numbers
    for i in range(len(list_of_Nums)):
        
        #Turns each element of the list into a float and adds to create a sum
        sum_of_Nums += float(list_of_Nums[i])

    #Divides the sum by the number elements in the list to calculate the mean
    mean = sum_of_Nums / len(list_of_Nums)
    
    #Returns the calculated mean to location of function call
    return mean

#Function to calculate the median of a set of numbers
def _Find_Median_(list_of_Nums):

    #Local Declarations------------------------------------
    median = 0   #Stores the calculated median
    mid_Num = 0  #Stores the middle number of the list of numbers

    #Local Statements--------------------------------------

    #For loop to declare each element in the set a float
    for i in range(len(list_of_Nums)):
         
         #Declares each element in list_of_nums a float
         list_of_Nums[i] = float(list_of_Nums[i])

    #List method to sort elements from least to greatest value
    list_of_Nums.sort()
    
    #Calculates the for the middle index number
    mid_Num = len(list_of_Nums) // 2

    #If else statements to determine if the number of elements in the list are
    # odd or even
    if (len(list_of_Nums) % 2 == 1):

        #Declares that mid_num is the median because it is odd
        median = list_of_Nums[mid_Num]

        #Returns calculated median to function call
        return median

    else:
        
        #Calculates the median based on the mean of the two middle numbers
        # because the list is even
        median = (list_of_Nums[mid_Num] + list_of_Nums[mid_Num - 1]) / 2

        #Returns calculated median to function call
        return median

#Function to calculate the mode of a set of numbers        
def _Find_Mode_(list_of_Nums):

    #Local Declarations------------------------------------
    the_Max_Value = 2     #Stores the max value of occurrence of an element
    the_Current_Value = 0 #Stores the current max value to be tested
    mode_exist = 0        #Stores a value to determine if a mean exist
    dict_of_Nums = {}     #Stores the list of modes in the set of numbers
    mode = 0              #Stores the calculated largest valued mode

    #Local Statements--------------------------------------

    #For loop to declare each element a float
    for i in range(len(list_of_Nums)):
    
        #Declares each element in list_of_Nums a float
        list_of_Nums[i] = float(list_of_Nums[i])

    #Function to sort list of floats from least to greatest value
    list_of_Nums.sort()
    
    #For loop to determine the mode(s) of the set of numbers    
    for i in range(len(list_of_Nums)):

        #List method to count the number of the same the same elements in 
        # the list
        the_Current_Value = list_of_Nums.count(list_of_Nums[i])
        
        #If statement to determine if a mode(s) are present 
        if the_Current_Value >= the_Max_Value:
            
            #If statement to determine if previous modes are no longer valid
            if(the_Current_Value > the_Max_Value):

                #Method to clear all keys and values in the dictionary
                dict_of_Nums.clear()
                
                #Declares the_Max_Value as the new max
                the_Max_Value = the_Current_Value

            #Stores the the mode in a dictionary
            dict_of_Nums[i] = list_of_Nums[i]
            
            #Declares that a mode exist
            mode_exist = 1

    #If statements to determine if a mode is found or not
    if mode_exist == 1:

        #Returns list of mode(s) back to function call
        return list(dict_of_Nums.values())

    else:
        
        #Returns that a mode does not exist to function call
        return 0

#Main Function Call------------------------------------------------------------
main()

