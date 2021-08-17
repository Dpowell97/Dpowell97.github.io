"""
Program: IT101_Powell_Maze_Game_2.00.py
Date of Completed Version: 11/14/18
Author: Dustin Powell

-------------------------------------------------------------------------------
Objective: Program that allows the user to play a game to solve a maze.

-------------------------------------------------------------------------------
Program Algorithm:

Generation of the Maze(Completed 11/4/18, v1.00)
----------------------

1. A random number between is selected between a set range to determine the
size of the maze.

2. The size is then used to create the base grid for the maze.

3. The maze is generated using a version of Prim's Algorithm which determines
the allowed paths and walls of the maze.
(listed in references)

4. The start and end point of the maze is assigned to the corners of the maze.

Player Input(Completed 11/9/18, reworked in v2.00 for GUI)
------------

1. The keys W, A, S, and D will be allowed for the player to use to move a 
character in the maze.


GUI for Gameplay(Completed 11/14/18, v2.00)
----------------

1. The first screen will allow the user to select options to play the game or
quit the program.

2. When the user clicks the play button it generates a maze and loads the maze
to the screen for the user to play the game.

3. When the user solves the maze the player is given the option to play again
or quit the program.

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

Playlist of youtube videos of how to create tkinter GUI's
https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d

Link to how to clear GUI canvas.
https://stackoverflow.com/questions/15839491/how-to-clear-tkinter-canvas

Link to how to create multiple entities on GUI canvas and accept keyboard
input.
https://www.youtube.com/watch?v=Vo31f9RfCAk

Link to how to create a GUI window title.
https://stackoverflow.com/questions/51054522/new-window-title-in-tkinter

-------------------------------------------------------------------------------
Change Log:
-v0.01
    Uncommented and unreferenced version of program only with maze generation.
    
-v1.00 
    Added comments to the program .
    Added references and other information to program information
    Removed numpy library.
    Moved nested for loop to print the maze to main function

-v1.01
    Added function to determine the start and end point of the maze.
    Added loops and if statements in main to handle player movement in the maze.
    Added the win condition for the maze in main.
    Added section with known bugs in the program.

-v2.00
    Added new references to program information.
    Added section for GUI functions
    Added section for GUI statements for components of GUI.
    Added GUI functions to create a new maze and update the GUI.
    Added GUI function to exit the program.
    Updated player movement to work with the GUI using a function.
    Updated main to receive and argument for maze generation.
    Moved statement to generate maze size into function new_Game.
    Removed loops and if statements in main to handle player movement.
    
-------------------------------------------------------------------------------
Know Bugs In Program:

BUG ISSUE 1:
Extra layer of wall(s) existing next to the main exterior wall

-See BUG ISSUE 1 in code to see temporary fixes and section were bug occurs
-------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_Maze_Game_1.01.py
-------------------------------------------------------------------------------
Output v2.00:

   -GUI is used for user input and program display

-------------------------------------------------------------------------------
"""

#Libraries---------------------------------------------------------------------
import random
from tkinter import *
import tkinter.messagebox

#Main Function Declaration-----------------------------------------------------
def main(grid_rand_size):
    """Main Function"""

    #Local Declarations------------------------------------
    #grid_rand_size = 0 #Variable to store the generator grid size
    new_maze = [[]] #Variable to store the 2d array representing the maze
    finished_maze = [[]] #Variable to store the completed 2d with start
                         # and stop cells
    x_index = 1  #Variable to store the player's up and down position
    y_index = 1  #Variable to store the player's side to side position
    #Local Statements--------------------------------------

    #Function to create a randomly generated maze
    new_maze = _Create_Grid_(grid_rand_size)

    #Function to determine the stat and end point of the maze
    finished_maze = _determine_Start_End_(new_maze, grid_rand_size)

    #Sets the player to the start point
    finished_maze[x_index][y_index] = 5

    return finished_maze

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

def _determine_Start_End_(current_maze, grid_size):
    """Function to determine the start and end point of the maze"""

    #Sets the start point of the maze
    current_maze[1][1] = 2

    #BUG ISSUE 1 Temporary Fix
    #Sets the cell next the start point to a path
    current_maze[2][1] = 1
    
    #Sets the end point of the maze
    current_maze[grid_size-2][grid_size-2] = 3

    #BUG ISSUE 1 Temporary Fix
    #Sets the cell next to the end point to a path
    current_maze[grid_size-3][grid_size-2] = 1
            

    return current_maze

#GUI Functions-----------------------------------------------------------------

def new_Game():
    """Function to create a new game when clicks new game"""

    #Local Declarations------------------------------------

    global grid_rand_size #Variable to store the size of the generated maze.
    global finished_maze  #Variable to store the generated maze.
    global x_index #Variable to store the players current x index.
    global y_index #Variable to store the players current y index.

    x_index = 1 #Sets the player's position to the starting x index
    y_index = 1 #Sets the player's position to the starting y index
    
    #Local Statements--------------------------------------

    #Statement to determine the size of the maze
    grid_rand_size = random.randint(5,50)

    #Statement to clear the current canvas area in the GUI
    maze_area.delete("all")

    #Function call to create a new maze
    finished_maze = main(grid_rand_size)

    #Function call to draw and update the maze to GUI canvas
    game_Update()

def exit_Game():
    """Function to exit game when user clicks exit"""

    exit()

def game_Movement(event):
    
    #Local Declarations------------------------------------
    global x_index #Variable to store the player's current x index
    global y_index #Variable to store the player's current y index

    #Local Statements--------------------------------------
    
    #If statement to determine is the user inputted w to go up
    if event.char == "w":
    
        #If statement to determine if the player is allowed to move up
        if finished_maze[x_index - 1][y_index] != 0:

            #Sets current position back to path
            finished_maze[x_index][y_index] = 1
                
            #Decreases x_index by one to move the player
            x_index -= 1

            #Sets the player to the new cell
            finished_maze[x_index][y_index] = 5

            #Function call to draw and update the maze to GUI canvas
            game_Update()

    #If statement to determine is the user inputted s to go down
    if event.char == "s":

        #If statement to determine if the player is allowed to move down           
        if finished_maze[x_index + 1][y_index] != 0:
                    
            #Sets current position back to path
            finished_maze[x_index][y_index] = 1
                 
            #Increases x_index by one to move the player
            x_index += 1

            #Sets the player to the new cell
            finished_maze[x_index][y_index] = 5

            #Function call to draw and update the maze to GUI canvas
            game_Update()

    #If statement to determine is the user inputted d to go right
    if event.char == "d":

        #If statement to determine if the player is allowed to move right           
        if finished_maze[x_index][y_index + 1] != 0:
                    
            #Sets current position back to path
            finished_maze[x_index][y_index] = 1
                 
            #Increases x_index by one to move the player
            y_index += 1

            #Sets the player to the new cell
            finished_maze[x_index][y_index] = 5

            #Function call to draw and update the maze to GUI canvas
            game_Update()

    #If statement to determine is the user inputted a to go left
    if event.char == "a":

        #If statement to determine if the player is allowed to move left
        if finished_maze[x_index][y_index - 1] != 0:

            #Sets current position back to path
            finished_maze[x_index][y_index] = 1
                
            #Increases y_index by one to move the player    
            y_index -= 1

            #Sets the player to the new cell
            finished_maze[x_index][y_index] = 5

            #Function call to draw and update the maze to GUI canvas
            game_Update()

def game_Update():

    #Local Declarations------------------------------------
    x1 = 0 #Variable to store the current x coord of a rectangle
    y1 = 0 #Variable to store the current y coorf of a rectangle

    #Local Statements--------------------------------------

    #Statement to clear the current canvas area in the GUI
    maze_area.delete("all")

    #If statement to change start point back to green start once player has left
    # the start point.
    if x_index != 1 or y_index != 1:

        finished_maze[1][1] = 2

    #Nested for loop with if else statements to draw the maze to the GUI canvas
    for i in range(grid_rand_size):

        for j in range(grid_rand_size):

            #If the maze cell equals one it is a walkway
            if finished_maze[i][j] == 1:
                
                #Statement to print a walkway cell
                maze_area.create_rectangle(x1, y1, x1+10, y1+10, fill="white")

            #If the maze cell equals zero it is a wall
            elif finished_maze[i][j] == 0:

                #Statement to print a wall cell
                maze_area.create_rectangle(x1, y1, x1+10, y1+10, fill="black")

            #If the maze cell equals two it is the start cell
            elif finished_maze[i][j] == 2:

                #Statement to print the starting cell
                maze_area.create_rectangle(x1, y1, x1+10, y1+10, fill="green")

            #If the maze cell equals three is the finish cell 
            elif finished_maze[i][j] == 3:

                #Statement to print the finish cell
                maze_area.create_rectangle(x1, y1, x1+10, y1+10, fill="red")    

            #If the maze cell equals five is is the player current position
            elif finished_maze[i][j] == 5:
      
                #Statement to print the player's position
                maze_area.create_rectangle(x1, y1, x1+10, y1+10, fill="blue")

            #Increments the cells x position by 10 pixels
            x1 += 10


        #Increments the cells y position by 10 pixels
        y1 += 10
       
        #Sets the current x position back to pixel zero
        x1 = 0

    #If statement to determine if the maze has been solve and outputs
    # that the user has solved the maze and exits the game
    if x_index == grid_rand_size-2 and y_index == grid_rand_size-2:
      
        #Statement to display a window to ask the user a question stores the
        # response in variable answer
        answer = tkinter.messagebox.askquestion('You Win!', 'Maze Solved!\nWould you like to play again?')

        #If else statement to handle the users response
        if answer == 'yes':

            #Function call to create a new game
            new_Game()

        else:

            #Function call to exit the game
            exit_Game()

#GUI Statements----------------------------------------------------------------

#Statement to create an instance of the tkinter GUI
root = Tk()

#Statement to set the window's name
root.title("Dustin Powell's Maze Game v2.00")

#Statements to determine the size and position of the GUI canvas for the maze
maze_area = Canvas(root, width = 500, height = 500)
maze_area.grid(row = 0, column = 3, columnspan = 14, rowspan = 14)

#Statements 
game_options = Label(root, text = "Game Options",fg = "Black")
game_options.grid(row = 0, columnspan = 2)

#Statements to create and position the New Game and Exit buttons
# which call a function when clicked.
play_button = Button(root, text = "New Game", command = new_Game )
play_button.grid(row = 1, columnspan = 2)
exit_button = Button(root, text="Exit", command = exit_Game )
exit_button.grid(row = 2, columnspan = 2)

#Statements to create and position for the title of the game legend
game_legend = Label(root, text = "Symbols", fg = "Black")
game_legend.grid(row = 3, columnspan = 2)

#Statements to create and position labels for the symbols of the game legend
player_label = Label(root, text = "Player:", fg = "Black")
player_label.grid(row = 4, column = 0, sticky = W)

wall_label = Label(root, text = "Wall:", fg = "Black")
wall_label.grid(row = 5, column = 0, sticky = W)

walkway_label = Label(root, text = "Walkway:", fg = "Black")
walkway_label.grid(row = 6, column = 0, sticky = W)

start_label = Label(root, text = "Start:", fg = "Black")
start_label.grid(row = 7, column = 0, sticky = W)

finish_label = Label(root, text = "Finish:", fg = "Black")
finish_label.grid(row = 8, column = 0, sticky = W)

#Statements to create and position the symbols for the game legend
player_symbol = Label(root, text = "    ", bg = "blue")
player_symbol.grid(row = 4, column = 1)

wall_symbol = Label(root, text = "    ", bg = "black")
wall_symbol.grid(row = 5, column = 1)

walkway_symbol = Label(root, text = "    ", bg = "white")
walkway_symbol.grid(row = 6, column = 1)

start_symbol = Label(root, text = "    ", bg = "green")
start_symbol.grid(row = 7, column = 1)

finish_symbol = Label(root, text = "    ", bg = "red")
finish_symbol.grid(row = 8, column = 1)

#Statements to create and position for the keys allowed for player movement
game_moveLabel = Label(root, text = "Player Moves", fg = "Black")
game_moveLabel.grid(row = 9, columnspan = 2)

move_upLabel = Label(root, text = "W:", fg = "Black")
move_upLabel.grid(row = 10, column = 0, sticky = W)

move_dwLabel = Label(root, text = "S:", fg = "Black")
move_dwLabel.grid(row = 11, column = 0, sticky = W)

move_lfLabel = Label(root, text = "A:", fg = "Black")
move_lfLabel.grid(row = 12, column = 0, sticky = W)

move_rhLabel = Label(root, text = "D:", fg = "Black")
move_rhLabel.grid(row = 13, column = 0, sticky = W)

#Statements to create and position the function of the keys for player movement
move_upAct = Label(root, text = "Up", fg = "Black")
move_upAct.grid(row = 10, column = 1)

move_dwAct = Label(root, text = "Down", fg = "Black")
move_dwAct.grid(row = 11, column = 1)

move_lfAct = Label(root, text = "Left", fg = "Black")
move_lfAct.grid(row = 12, column = 1)

move_rhAct = Label(root, text = "Right", fg = "Black")
move_rhAct.grid(row = 13, column = 1)

#Statement to bind keyboard input to the GUI and call a function when
# a key is pressed.
root.bind("<Key>", game_Movement) 

#Statement to loop for the GUI to stay open.
root.mainloop()









