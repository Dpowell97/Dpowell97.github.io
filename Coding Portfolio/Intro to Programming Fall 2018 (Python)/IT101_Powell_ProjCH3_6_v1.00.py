"""
Program: IT101_Powell_ProjCH3_6_v1.00.py
Due Date: 09/20/18
Author: Dustin Powell

--------------------------------------------------------------------------------
Objective: To output a n number of iterations of the aproximation of pi

--------------------------------------------------------------------------------
Project Algorithm:
1. Define the constants of the forumla.
2. Prompt user for the number of iterations to run.
3. Calcualte pi/4 to n number of iterations.
4. Calculate pi/4 from python to show the differences between ouputs
5. Output the final sum and number of iterations performed

--------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
--------------------------------------------------------------------------------
Acknowledgment Notes:
The code use is refered from the course book and in class discussion

--------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of the program.
--------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_ProjCH3_6_v1.00.py
--------------------------------------------------------------------------------
Output:
-v1.00

This programs aproximates pi/4 to i number of iterations.

Please enter the number of iterations to be performed: 5

Iteration #:  Aproximation of pi/4
------------------------------------
         1 :  1.00000000000000000000
         2 :  0.66666666666666674068
         3 :  0.86666666666666669627
         4 :  0.72380952380952390257
         5 :  0.83492063492063506303
------------------------------------

   Program results and comparisons   
-------------------------------------
Pyhton's Aproximation of pi/4:  0.7853981633974483
Total number of iterations performed:  5
Aproximation calculated after 5 iterations:  0.8349206349206351

--------------------------------------------------------------------------------
"""
#Libaries-----------------------------------------------------------------------
import math 

#Global Constants---------------------------------------------------------------
#NONE

#Main Function Decleration------------------------------------------------------
def main():

    #Local Declerations-------------------------------------
    i = 0 #Number of iterations to be perfomred
    piAprox = 0 #Varrible to store the aproximation of PI to i iterations
    countUp = 0 #Varrible to count number of iterations and increase fractions
    #Local Statments----------------------------------------

    #Displays program information
    print("This programs aproximates pi/4 to i number of iterations.\n")
    
    #Prompts user to input the number of iterations to be perfomred
    i = int(input("Please enter the number of iterations to be performed: "))

    #Displays header for program output
    print("\nIteration #:  Aproximation of pi/4")
    print("------------------------------------")
    
    #For loop to go through i iterations
    for i in range(i):
        
        #Loop counter and used to increase fraction denominators
        countUp += 1
        
        #If else statment to determine if i is zero
        if ( i == 0):
       
            #Sets the first defined iteration of i to 1
            piAprox = countUp

        else:
            
            #Nested if else statment to determine if i is even or odd 
            if ( i % 2 == 1):
                
                #Adds countUp value to i to determine denominator
                i = i + countUp
             
                #Subtracts 1/i from current sum
                piAprox = piAprox - (1/i)
                
                #Subtracts countUp value from i to allow for next denomintor 
                i = i - countUp

            else:
                #Adds countUp value to i to determine denominator
                i = i + countUp

                #Adds 1/i to current sum
                piAprox = piAprox + (1/i)
           
                #Subtracts countUp value from i to allow for next denomintor
                i = i - countUp

       #Outputs the current value of the current iterations
        print("%10d :  %1.20f" % (countUp, piAprox))
    
    #Calcualtes the python default for Pi/4
    pythonPi = math.pi/4
    

    #Displays program closing information
    print("------------------------------------")
    print("\n         Program Results   ")
    print("-------------------------------------")
    print("Pyhton's Aproximation of pi/4: ", pythonPi)
    print("Total number of iterations performed: ", countUp)
    print("Aproximation calculated after",countUp, "iterations: ", piAprox)

#Function Declerations----------------------------------------------------------
#NONE


#Main Function Call-------------------------------------------------------------
main()
















