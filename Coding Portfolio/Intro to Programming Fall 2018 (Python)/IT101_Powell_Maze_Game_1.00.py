"""
Program: IT101_Powell_Maze_Game_1.00.py
Due Date: 11/6/18
Author: Dustin Powell

-------------------------------------------------------------------------------
Objective: Program that allows the user to play a game to solve a maze or use
a neural network to solve the maze.

-------------------------------------------------------------------------------
Program Algorithm:

Generation of the Maze
----------------------

1. A random number between is selected between a set range to determine the
size of the maze.

2. The size is then used to create the base grid for the maze.

3. The maze is generated using a version of Prim's Algorithm which determines
the allowed paths and walls of the maze.
(listed in references)

4. The start and end point of the maze is assigned to the corners of the maze.

Player Input
------------

1. The keys W, A, S, and D will be allowed for the player to use to move a 
character in the maze.


GUI for Gameplay
----------------

1. The first screen will allow the user to select options to play the game or
quit the program.

2. When the user clicks the play button it generates a maze and loads the maze
to the screen for the user to play the game.

3. When the user solves the maze the player is given the option to play again
or quit the program.


Neural Network/Machine Learning (Using tensorflow and if time permits)
-----------------------------------------------------------------------

1. Determine the neural network to use.

2. Determine what is needed to make the neural network work with the game.

3. Option for user to select the neural network to play the maze game will
be added.

4. Determine what data is to be outputted from running the neural network.

-------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
-------------------------------------------------------------------------------
Acknowledgment Notes:
Course book was used for syntax and some methods.
Link to version of Prim's Algorithm going to be used from the the 
stackoverflow answer.
https://stackoverflow.com/questions/29739751/implementing-a-randomly-generated-
maze-using-prims-algorithm

Link to way to create a 2d array in python.
https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-
array-in-python

-------------------------------------------------------------------------------
Change Log:
-v0.01
    Uncommented and unreferenced version of program only with maze generation.
    
-v1.00 
    Added comments to the program .
    Added references and other information to program information
    Removed numpy library.
    Moved nested for loop to print the maze to main function
-------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_Maze_Game_1.00.py
-------------------------------------------------------------------------------
Output v1.00:

X X X X X X X X X X X X  
X X                   X  
X X   X X X   X X X   X  
X X       X       X   X  
X X   X X X X X   X X X  
X X   X       X       X  
X X   X   X   X X X   X  
X X   X   X   X       X  
X X   X   X   X   X   X  
X X   X   X       X   X  
X X X X X X X X X X X X  
X X X X X X X X X X X X 

-------------------------------------------------------------------------------
"""
#Libraries---------------------------------------------------------------------
import random

#Main Function Declaration-----------------------------------------------------
def main():
    """Main Function"""

    #Local Declarations------------------------------------
    grid_rand_size = 0 #Variable to store the generator grid size
    new_maze = [[]] #Variable to store the 2d array representing the maze

    #Local Statements--------------------------------------
    
    #Statement to determine the size of the maze
    grid_rand_size = random.randint(5,60)

    #Function to create a randomly generated maze
    new_maze = _Create_Grid_(grid_rand_size)

    #Nested for loop with if else statement to print the maze to the screen
    for i in range(grid_rand_size):

        for j in range(grid_rand_size):
  
            if new_maze[i][j] == 1:
                print(" ", end = " ")

            else:

                print("X", end = " ")

        print(" ")


#Function Declarations---------------------------------------------------------
def _Create_Grid_(grid_size):
    """Function to create the maze for the player to solve"""

    #Local Declarations------------------------------------
    #Variable to store the base 2d array to represent the maze
    base_grid = [[0 for i in range(grid_size)] for j in range(grid_size)]

    #Local Statements--------------------------------------

    #Nested for loops to set all values in base_grid to zero to create 2d array
    # of walls.
    for i in range(grid_size):

        for j in range(grid_size):

            base_grid[i][j] = 0

    #Picks a random number for each index to start creating a maze for a
    # the set of i        
    ran_I = random.randint(1, grid_size - 2)
    ran_J = random.randint(1, grid_size - 2)


    #Sets the randomly picked cell to a walkway            
    base_grid[ran_I][ran_J] = 1

    #Function call to determine which cells are walkways and walls
    base_grid = _determine_Walls_(ran_I, ran_J, base_grid, grid_size)
                    
    return base_grid

def _determine_North_(current_grid, index_I, index_J, current_size):
    """Function to determine if a north cell in distance 2 exist"""

    #Local Declarations------------------------------------
    north = False    #Variable to store if north cell exist or not

    #Local Statements--------------------------------------

    #Try except statement to deal with errors that occur from being out list
    # range
    try:
        
        #Nested if statements to determine if the distance 2 cell is a wall,
        # and if the indexes are in the allowed range
        if current_grid[index_I - 2][index_J] == 0:

            if index_I-2>0 and index_I-2<current_size-1: 

                if index_J>0 and index_J<current_size-1:

                    north = True

    except:

        north = False

    return north

def _determine_South_(current_grid, index_I, index_J, current_size):
    """Function to determine if a south cell in distance 2 exist"""

    #Local Declarations------------------------------------
    south = False    #Variable to store if south cell exist or not

    #Local Statements--------------------------------------

    #Try except statement to deal with errors that occur from being out list
    # range
    try:
    
        #Nested if statements to determine if the distance 2 cell is a wall,
        # and if the indexes are in the allowed range
        if current_grid[index_I + 2][index_J] == 0:
        
            if index_I+2>0 and index_I+2<current_size-1:
 
                if index_J>0 and index_J<current_size-1:
                   
                    south = True
                
    except:

        south = False

    return south

def _determine_East_(current_grid, index_I, index_J, current_size):
    """Function to determine if a east cell in distance 2 exist"""

    #Local Declarations------------------------------------
    east = False    #Variable to store if east cell exist or not

    #Local Statements--------------------------------------

    #Try except statement to deal with errors that occur from being out list
    # range
    try:

        #Nested if statements to determine if the distance 2 cell is a wall,
        # and if the indexes are in the allowed range
        if current_grid[index_I][index_J + 2] == 0:

            if index_I>0 and index_I<current_size-1:

                if index_J+2>0 and index_J+2<current_size-1:

                    east = True

    except:
        
        east = False

    return east
    

def _determine_West_(current_grid, index_I, index_J, current_size):
    """Function to determine if a east cell in distance 2 exist"""

    #Local Declarations------------------------------------
    west = False    #Variable to store if west cell exist or not

    #Local Statements--------------------------------------
    
    #Try except statement to deal with errors that occur from being out list
    # range
    try:

        #Nested if statements to determine if the distance 2 cell is a wall,
        # and if the indexes are in the allowed range
        if current_grid[index_I][index_J - 2] == 0:

            if index_I>0 and index_I<current_size-1:

                if index_J-2>0 and index_J-2<current_size-1:

                    west = True

    except:
        
        west = False

    return west


def _determine_Walls_(index_I, index_J, current_grid, current_size):
    """Function to determine if a cell is a walkway based on walls"""

    #Local Declarations------------------------------------
    south = False    #Variable to store if south cell exist or not
    north = False    #Variable to store if north cell exist or not
    east = False     #Variable to store if east cell exist or not
    west = False     #Variable to store if west cell exist or not
    rand_flag = True #Variable to store if a random number has 
                     # been called once

    #Local Statements--------------------------------------

    #Function calls to determine which cells exist or not
    north = _determine_North_(current_grid, index_I, index_J, current_size)

    south = _determine_South_(current_grid, index_I, index_J, current_size)

    east = _determine_East_(current_grid, index_I, index_J, current_size)

    west = _determine_West_(current_grid, index_I, index_J, current_size)
    
    #If else statement to determine if all distance 2 cells that are walls
    # exist.
    if (north or south or east or west) == False:

        return current_grid

    else:

        #While loop to calculate distance 2 cells and create walkways
        while True:

            #If statement determine if a random number should be generated
            if rand_flag == True:

                #Statement to generate a random number for which cell to be a
                # wall
                rand_front = random.randint(1,4)

            #If statement to determine if the wall is selected or is an
            # allowed cell
            if (rand_front == 1 or rand_front == 0) and north == True:
                
                #Flag to determine that a random cell has been selected
                rand_flag = False

                #Sets random cell picked to zero to allow other cells to become
                # walkways or walls.
                rand_front = 0
             
                #Sets a neighbor to a walkway to the current 
                # walkway in distance 2
                current_grid[index_I - 1][index_J] = 1

                #Sets current cell in distance 2 to current walkway to a walkway
                current_grid[index_I - 2][index_J] = 1

                #Decreases index I by 2 to a new current position
                index_I -= 2

                #Function call to calculate the current distance 2 walls
                # at the current position
                current_grid = _determine_Walls_(index_I, index_J, current_grid, current_size)

                #Increases index I by 2 to the previous current position
                index_I += 2

                #Function calls to determine which cells exist or not after recursion
                # backtracking.
                north = _determine_North_(current_grid, index_I, index_J, current_size)
                south = _determine_South_(current_grid, index_I, index_J, current_size)
                east = _determine_East_(current_grid, index_I, index_J, current_size)
                west = _determine_West_(current_grid, index_I, index_J, current_size)

            #If statement to determine if the wall is selected or is an
            # allowed cell            
            if (rand_front == 2 or rand_front == 0) and south == True:

                #Flag to determine that a random cell has been selected
                rand_flag = False

                #Sets random cell picked to zero to allow other cells to become
                # walkways or walls.
                rand_front = 0

                #Sets a neighbor to a walkway to the current 
                # walkway in distance 2
                current_grid[index_I + 1][index_J] = 1

                #Sets current cell in distance 2 to current walkway to a walkway
                current_grid[index_I + 2][index_J] = 1

                #Increases index I by 2 to the new current position
                index_I += 2

                current_grid = _determine_Walls_(index_I, index_J, current_grid, current_size)

                #Decreases index I by 2 to a previous current position
                index_I -= 2

                #Function calls to determine which cells exist or not after recursion
                # backtracking.
                north = _determine_North_(current_grid, index_I, index_J, current_size)

                south = _determine_South_(current_grid, index_I, index_J, current_size)

                east = _determine_East_(current_grid, index_I, index_J, current_size)

                west = _determine_West_(current_grid, index_I, index_J, current_size)

            #If statement to determine if the wall is selected or is an
            # allowed cell
            if (rand_front == 3 or rand_front == 0) and east == True:

                #Flag to determine that a random cell has been selected
                rand_flag = False
                
                #Sets random cell picked to zero to allow other cells to become
                # walkways or walls.
                rand_front = 0

                #Sets a neighbor to a walkway to the current 
                # walkway in distance 2
                current_grid[index_I][index_J + 1] = 1

                #Sets current cell in distance 2 to current walkway to a walkway
                current_grid[index_I][index_J + 2] = 1

                #Increases index J by 2 to the new current position
                index_J += 2

                current_grid = _determine_Walls_(index_I, index_J, current_grid, current_size)

                #Decreases index J by 2 to a previous current position
                index_J -= 2

                #Function calls to determine which cells exist or not after recursion
                # backtracking.
                north = _determine_North_(current_grid, index_I, index_J, current_size)

                south = _determine_South_(current_grid, index_I, index_J, current_size)

                east = _determine_East_(current_grid, index_I, index_J, current_size)

                west = _determine_West_(current_grid, index_I, index_J, current_size)

            #If statement to determine if the wall is selected or is an
            # allowed cell
            if (rand_front == 4 or rand_front == 0) and west == True:

                #Flag to determine that a random cell has been selected
                rand_flag = False
                
                #Sets random cell picked to zero to allow other cells to become
                # walkways or walls.
                rand_front = 0
                
                #Sets a neighbor to a walkway to the current 
                # walkway in distance 2
                current_grid[index_I][index_J - 1] = 1

                #Sets current cell in distance 2 to current walkway to a walkway
                current_grid[index_I][index_J - 2] = 1

                #Decreases index J by 2 to a new current position
                index_J -= 2

                current_grid = _determine_Walls_(index_I, index_J, current_grid, current_size)

                #Increases index J by 2 to the previous current position
                index_J += 2

                #Function calls to determine which cells exist or not after recursion
                # backtracking.
                north = _determine_North_(current_grid, index_I, index_J, current_size)

                south = _determine_South_(current_grid, index_I, index_J, current_size)

                east = _determine_East_(current_grid, index_I, index_J, current_size)

                west = _determine_West_(current_grid, index_I, index_J, current_size)

            #If statement to break loop when all distance 2 cells are walkways
            if north == False and south == False and east == False and west == False:

                break
    
    return current_grid

#Main Function Call------------------------------------------------------------
main()









