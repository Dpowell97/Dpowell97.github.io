"""
Program: IT101_Powell_Ch7Proj3_1.00.py
Due Date: 11/13/18
Author: Dustin Powell

-------------------------------------------------------------------------------
Objective: Write a program using turtle to output levels 0 - 2 of the Koch's
snowflake.
-------------------------------------------------------------------------------
Project Algorithm:
1. Receive user inputted level
2. Determine the distance of lines to be drawn
3. Determine if a bump is needed to created at a drawn line.
4. Draw the fractal from the distance and number of bumps needed.
5. Prompt user to exit the program.

-------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
-------------------------------------------------------------------------------
Acknowledgment Notes:
In class discussion was used to help with the project.
Syntax and examples from the course book was also used.
Snippets of code from previous projects are used.

-------------------------------------------------------------------------------
Change Log:
v1.00
    First completed version of the program


-------------------------------------------------------------------------------
Compiler Used:

python3 IT101_Powell_Ch7Proj3_1.00.py
-------------------------------------------------------------------------------
Sample Output:
Koch Snowflake Program
----------------------

Please enter a level between 0 - 2: 1
Telling turtle to wake up...
Fractal complete, press any key to exit.

-------------------------------------------------------------------------------
"""

#Libraries---------------------------------------------------------------------
from turtle import *

#Main Function Declaration-----------------------------------------------------
def main():
    """Main function of the program"""

    #Local Declarations------------------------------------
    level = 0        #Variable to store the user inputted level
    num_of_loops = 0 #Variable to store the number of loops performed
    #Local Statements--------------------------------------

    #Print statements for the program header
    print("Koch Snowflake Program")
    print("----------------------")
    print()
    
    #While loop to test with try statement to determine if the user inputted
    # a valid integer for the level
    while True:

        try:

            level = int(input("Please enter a level between 0 - 2: "))

            print("Telling turtle to wake up...")

            break

        except:

            print("Please enter a valid value")

    #Creates an instance of turtle
    t = Turtle()

    #Function call to create a fractal at the given level
    _draw_Fractal_Line_(t, level, num_of_loops)
    

#Function Declarations---------------------------------------------------------
def _draw_Fractal_Line_(t, level, num_of_loops):

    #Local Declarations------------------------------------
    distance = 0 #Variable to store the distance for a line to travel
    exit_varriable = 0 #Variable to store a user randomly inputted key to exit
                       # the program.
    #Local Statements--------------------------------------

    #Function call to determine the distance of each line with the given level
    distance = _determine_distance_(level)

    #If else statement to determine what statements to performed based on the
    # level
    if level == 0:
        
        #Turtle methods to draw and change direction to create the fractal
        t.forward(distance)
        t.left(-120)

        #If else statement to determine if the fractal is complete and
        # end the recursive loop
        if num_of_loops < 3:

            num_of_loops += 1

            _draw_Fractal_Line_(t, level, num_of_loops)

        else:
            
           exit_varriable = input("Fractal complete, press any key to exit.")

    else:
        
        #Turtle methods to draw a line of the fractal
        t.forward(distance)
        
        #If statement to determine if a bump is needed to be created
        if level >= 2:

            #Turtle methods to draw and change direction to create the bump
            t.left(60)
            t.forward(distance)
            t.left(-120)
            t.forward(distance)
            t.left(60)
            t.forward(distance)

        #Turtle methods to change directions and draw a line of the fractal
        t.left(-120)
        t.forward(distance)

        #If statement to determine if a bump is needed to be created
        if level >= 2:

            #Turtle methods to draw and change direction to create the bump
            t.left(60)
            t.forward(distance)
            t.left(-120)
            t.forward(distance)
            t.left(60)
            t.forward(distance)

        #Turtle method to change direction
        t.left(60)
        
        #If else statement to determine if the fractal is complete and
        # end the recursive loop
        if num_of_loops < 8:

            num_of_loops += 1

            _draw_Fractal_Line_(t, level, num_of_loops)
        else:
            
           exit_varriable = input("Fractal complete, press any key to exit.")
    
def _determine_distance_(level):
    """Function to determine the distance of line to draw"""

    #Local Declarations------------------------------------
    distance = 200 #Variable to store the distance of the line to be drawn
    #Local Statements--------------------------------------
    
    #If else statement to determine which operations to be performed to 
    # to determine the distance
    if level == 0:

        return distance

    else:

        #For loop the shorten the distance by 1/3 each level
        for i in range(level):

            distance //= 3

        return distance


#Main Function Call------------------------------------------------------------
main()

