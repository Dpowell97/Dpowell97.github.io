"""
Program: IT101_Powell_Maze_Game_1.00.py
Due Date: 10/11/18
Author: Dustin Powell

-------------------------------------------------------------------------------
Objective: Write a program the shifts bit string to the left

-------------------------------------------------------------------------------
Program Algorithm:


-------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
-------------------------------------------------------------------------------
Acknowledgment Notes:
Course book was used for syntax

-------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of the program.
-------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 
-------------------------------------------------------------------------------
Output:



-------------------------------------------------------------------------------
"""
#Libraries---------------------------------------------------------------------
import random
import numpy as np

def main():

    grid_rand_size = random.randint(5,60)

    new_grid = _Create_Grid_(grid_rand_size)


#Function Declerations---------------------------------------------------------
def _Create_Grid_(grid_size):

    grid_X = 0
    grid_Y = 0
    base_grid = [[0 for i in range(grid_size)] for j in range(grid_size)]

    for i in range(grid_size):

        for j in range(grid_size):

            base_grid[i][j] = 0

            
    ran_I = random.randint(1, grid_size - 2)

    ran_J = random.randint(1, grid_size - 2)
            
    base_grid[ran_I][ran_J] = 1

    base_grid = _determine_Walls_(ran_I, ran_J, base_grid, grid_size)
                    

    for i in range(grid_size):

        for j in range(grid_size):
  
            if base_grid[i][j] == 1:
                print(" ", end = " ")

            else:

                print("X", end = " ")

        print(" ")

def _determine_North_(current_grid, index_I, index_J, current_size):

    north = False

    try:

        if current_grid[index_I - 2][index_J] == 0:

            if index_I-2>0 and index_I-2<current_size-1: 

                if index_J>0 and index_J<current_size-1:

                    north = True

    except:

        north = False

    return north

def _determine_South_(current_grid, index_I, index_J, current_size):

    south = False

    try:
    
        if current_grid[index_I + 2][index_J] == 0:
        
            if index_I+2>0 and index_I+2<current_size-1:
 
                if index_J>0 and index_J<current_size-1:
                   
                    south = True
                
    except:

        south = False

    return south

def _determine_East_(current_grid, index_I, index_J, current_size):

    east = False

    try:

        if current_grid[index_I][index_J + 2] == 0:

            if index_I>0 and index_I<current_size-1:

                if index_J+2>0 and index_J+2<current_size-1:

                    east = True

    except:
        
        east = False

    return east
    

def _determine_West_(current_grid, index_I, index_J, current_size):

    west = False


    try:

        if current_grid[index_I][index_J - 2] == 0:

            if index_I>0 and index_I<current_size-1:

                if index_J-2>0 and index_J-2<current_size-1:
         
                    

                    frontier_test = True

                    west = True

    except:
        
        west = False

    return west


def _determine_Walls_(index_I, index_J, current_grid, current_size):

    south = False
    north = False
    east = False
    west = False
    rand_flag = True

    north = _determine_North_(current_grid, index_I, index_J, current_size)
    south = _determine_South_(current_grid, index_I, index_J, current_size)
    east = _determine_East_(current_grid, index_I, index_J, current_size)
    west = _determine_West_(current_grid, index_I, index_J, current_size)
    

    if (north or south or east or west) == False:

        return current_grid

    else:

        while True:

            
            if rand_flag == True:

                rand_front = random.randint(1,4)

            if (rand_front == 1 or rand_front == 0) and north == True:
            
                rand_flag = False

                rand_front = 0
             
                current_grid[index_I - 1][index_J] = 1

                current_grid[index_I - 2][index_J] = 1

                index_I -= 2

                current_grid = _determine_Walls_(index_I, index_J, current_grid, current_size)

                index_I += 2

                north = _determine_North_(current_grid, index_I, index_J, current_size)
                south = _determine_South_(current_grid, index_I, index_J, current_size)
                east = _determine_East_(current_grid, index_I, index_J, current_size)
                west = _determine_West_(current_grid, index_I, index_J, current_size)
            
            if (rand_front == 2 or rand_front == 0) and south == True:

                rand_flag = False

                rand_front = 0

                current_grid[index_I + 1][index_J] = 1

                current_grid[index_I + 2][index_J] = 1

                index_I += 2

                current_grid = _determine_Walls_(index_I, index_J, current_grid, current_size)

                index_I -= 2

                north = _determine_North_(current_grid, index_I, index_J, current_size)
                south = _determine_South_(current_grid, index_I, index_J, current_size)
                east = _determine_East_(current_grid, index_I, index_J, current_size)
                west = _determine_West_(current_grid, index_I, index_J, current_size)

            if (rand_front == 3 or rand_front == 0) and east == True:

                rand_flag = False

                rand_front = 0

                current_grid[index_I][index_J + 1] = 1

                current_grid[index_I][index_J + 2] = 1

                index_J += 2

                current_grid = _determine_Walls_(index_I, index_J, current_grid, current_size)

                index_J -= 2

                north = _determine_North_(current_grid, index_I, index_J, current_size)
                south = _determine_South_(current_grid, index_I, index_J, current_size)
                east = _determine_East_(current_grid, index_I, index_J, current_size)
                west = _determine_West_(current_grid, index_I, index_J, current_size)

            if (rand_front == 4 or rand_front == 0) and west == True:

                rand_flag = False

                rand_front = 0

                current_grid[index_I][index_J - 1] = 1

                current_grid[index_I][index_J - 2] = 1

                index_J -= 2

                current_grid = _determine_Walls_(index_I, index_J, current_grid, current_size)

                index_J += 2

                north = _determine_North_(current_grid, index_I, index_J, current_size)
                south = _determine_South_(current_grid, index_I, index_J, current_size)
                east = _determine_East_(current_grid, index_I, index_J, current_size)
                west = _determine_West_(current_grid, index_I, index_J, current_size)


            if north == False and south == False and east == False and west == False:

                break
       
    return current_grid

main()









