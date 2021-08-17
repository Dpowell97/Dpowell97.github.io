//Program: Powell_Maze_v1.05
//Due Date: 04/16/18
//Author: Dustin Powell
//Objective: Create a program that randomly generates a maze of n x n size, and
//then solves the maze with the shortest path. The maze must be represented 
//graphically

/*Current Project Algorithm

1. Generate a Maze of n x n size.
    a. Generate a 2d array with randomly generated size
	   - Call function from main to create a 2d array.
	   - Use malloc to allocate enough memory for the
		 2d array.
	   - Set the values of 2d array to zero for later use.
	   - Return to main with 2d array.
	   
	b. Randomly generate walls for the grid.
	   - Call function from main using the 2d array.
	   - Randomly generate a value for walls in 
	     the 2d array.
	   - Declare the exterior walls of the 2d array.
	   - Declare start and end points of array to
	     unvisited paths.
	   - Allow for multiple paths and dead ends by 
	     removing large areas of walls using random 
		 generated selection.
	   - Return the 2d array to main with walls.
	
2. Traverse The Maze
	a. Use depth first search traversal to solve for the maze.
	   - Call a function from main using the 2d array.
	   - Calls a second function from current function to
	     set current vertex to visited.
	   - Determine vertex that is unvisited the recursively
		 call function again to mark vertex as visited.
	   - When end point is marked as visited traversal stops.
	   - Seconds function returns to first then first function
		 returns to main with 2d array with walls and path to
		 end point.
		 
3. Graphical Representation
	a. Display 2d array using c code.
		- At start of program in main print out program header.
		- After print maze information such as what values mean.
		- If maze generated has no solution recall function to
		  generate walls and traverse 2d array again.
		- When a maze with a solution is found print the 2d array.
	b. Represent the maze in another form.
	    - Function call from main using 2d array.
	    - Have the function write a file to represent the graph visual.
		- Have the function program run the visual.
		- Function returns to main.
		- Program terminates.
			
*/
//Honor Code: On my honor, I have neither given nor received unauthorized or 
//unacknowledged aid on this academic work and I am unaware of any violations 
//of this code by others.
//Signed: Dustin Powell

//Acknowledgment Notes:
//Parts of program come from in class discussion, textbook,
//and use in previous assignments.
//The application of malloc  and multiple pointers comes from:
//https://www.geeksforgeeks.org/dynamically-allocate-2d-array-c/
//Usage of time functions come from us in other assignments. Link below
//https://www.tutorialspoint.com/c_standard_library/c_function_difftime.htm
//Usage of statements to write files come from:
//https://www.youtube.com/watch?v=38I_AUMpKpQ
//Examples on how to write HTML comes from link below:
//https://www.youtube.com/watch?v=UB1O30fR-EE
//Examples on how to use HTML attributes comes from link below:
//https://www.w3schools.com/html/html_attributes.asp

/*Change Log-------------------------------------------------------------------
v1 03/19/18
- Added Program comments and information
- Added Main function
- Added function _Create_Movement_Grid_ to generate grid
- Added function _Create_Walls_ to generate walls for the grid

v1.01 3/21/18
- Fixed _Create_Walls_ to create walls in proper place in terms of a matrix.
- Adjusted comments for _Create_Walls_.

v1.02 3/26/18
- Added functions _Depth_First_Search_Traversal_ to
- Added function _Depth_First_Search_
- Created comments for new functions
- Updated Algorithm 
- Updated Program Output
- Error found with generating a maze bigger than 4 x 4 will be fixed next
  next update.
  
v1.03 4/2/18
- Simplified how walls work and rewrote function  _Create_Walls_ in doing
  so fixed crashing issue.
- Adjusted _Depth_First_Search_ and _Depth_First_Search_Traversal_ to work
  with new output of _Create_Walls_
- Added nested if and else if statements to prevent large blocks of walls.
- Added do while loops to main to only allow solved mazes and mazes sizes 
  bigger then 2x2
- Updated output information with program header and maze information
- Added possibility of program to terminate if a maze is not generated
  in 45 seconds.
- Updated program algorithm.

v1.04 4/9/18
- Removed a nested for loop in _Depth_First_Search_Traversal_ to cut down
  on total runtime.
- Added function _Display_Maze_ to write an HTML file to view maze output
- Removed and reworked original program output statements

v1.05 4/16/18
- Added updated HTML output to use colored boxes to represent maze.
- Removed Nested If statements to remove large blocks of walls and replaced
  the statements with a way to allow more paths and dead ends.
- Re-added nested for loops for _Depth_First_Search_Traversal_.
- Increased possible size of maze to 75 x 75.
- Removed if statement to allow _Depth_First_Search_ to be only called once.

v1.06 4/18/18
- Reworked _Depth_First_Search_ by changing to consecutive if statements rather than
  nested if statements.
- Added a older version _Depth_First_Search_ reworked it to be _Create_Path_ that
  creates a single path from the results of _Depth_First_Search_.
- Updated program output to show results from _Depth_First_Search_ and _Create_Path_.
- Updated main to reflect changes from adding _Create_Path_

*/
//Compiler Used----------------------------------------------------------------
//gcc -o Powell_Maze_v1.06 Powell_Maze_v1.06.c

//Output ----------------------------------------------------------------------
/*
	
-Version 1.06
	Check HTML file Powell_MazeOutput_v1.06.html

*/
//Libraries---------------------------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


//Function Declarations--------------------------------------------------------
//Generates a n x n grid for movement
int _Create_Movement_Grid_(int num);

//Generates location of walls at each vertex
int _Create_Walls_(int num, int ** Grid);

//Function to check if current vertex is visited and determine if
//_Depth_First_Search_ is needed to be called
int _Depth_First_Search_Traversal_ (int ** Grid, int num);

//Function to set current vertex to visited and find near unvisited nodes
void _Depth_First_Search_(int ** Grid, int X_Coord, int Y_Coord, int num);

//Function to write program output in a HTML file
void _Display_Maze_(int ** Grid, int num, int Maze_Counter);

//Function to create a path that solves the maze
int _Create_Path_(int ** Grid, int X_Coord, int Y_Coord, int num);

//Main-------------------------------------------------------------------------
int main(void)
{
	//Local Decelerations----------------------------------
	int ** Grid; //2d array that contains grid 
	int num = 0; //Positive integer value to determine size of grids
	time_t seed_random, start, stop; //Time variable to seed random number generator,
	//and store variables to end program if time limit is reached.
	int Complete_Grid = 0; //Variable to determine if a solvable 
	double time_passed;    //Stores the amount of time passed since loop started
	int program_timeout = 0;  //Variable to end program if time goes 
	                          //passed 45 seconds
	int Maze_Counter = 0;  //Counts the number of loops to generate a maze
	int X_Coord, Y_Coord; //Integers to store current vertex in maze
	
	//Local Statements-------------------------------------

	//Random number generator
	srand((int) time(&seed_random));
	
	//do while loop to only allow random generated numbers greater than 2
	do
	{
		num = rand() % 76;
		
	}while(num <= 2);
	
	//Prints that maze generation has started
	printf("Generating a maze with a solution ...\n\n");
	
	//Function call to create movement grid
	Grid = _Create_Movement_Grid_(num);
	
	//Stores start time of generation
	time(&start);
	
	//Do while loop to only output completed mazes
	do
	{
		//Function call to create walls for the grid
		Grid = _Create_Walls_(num, Grid);

		//Function call to traverse grid
		Grid = _Depth_First_Search_Traversal_(Grid, num);
		
		//If statement to check is maze has been solved if not
		//current time taken is calculated
		if(Grid[num - 2][num - 2] == 2)
		{
			X_Coord = 1;
			Y_Coord = 1;
		
			Grid = _Create_Path_(Grid, X_Coord, Y_Coord, num);
			
			//If statement to determine if a path was created from DFS
			if(Grid[num - 2][num - 2] == 3)
			{
				//If maze has been solved Complete_Grid is set to 1
				Complete_Grid = 1;
			}
			else
			{
				//Maze loop counter
				Maze_Counter++;
				
				//Updates current time
				time(&stop);
				time_passed = difftime(stop, start);
			}
		}
		else
		{
			//Maze loop counter
			Maze_Counter++;
			
			//Stores 
			time(&stop);
			time_passed = difftime(stop, start);
		}
		
		//If statement to end loop if 45 seconds has passed
		if(45.00 < time_passed)
		{
			//Declares Complete_Grid to one to end loop
			Complete_Grid = 1;
			
			//Declares program_timeout to one to not output a maze
			program_timeout = 1;
		}
		
		
			
	}while(Complete_Grid != 1);
	
	//if statement to call function to write HTML file unless program
	//takes longer than 45 seconds
	if(program_timeout == 0)
	{
		
		_Display_Maze_(Grid, num, Maze_Counter);
		
		printf("Maze generated, please open HTML file.\n\n\n");
	}
	else
	{
		printf("Ending Program: Time to generate maze is longer than 45 seconds\n");
	}
	
	
}

//Function to that randomly Generates Size of grid for movement of maze
int _Create_Movement_Grid_(int num)
{
	//Local Decelerations----------------------------------
	int ** new_grid; //Store the generated 2d array
	
	//Local Statements-------------------------------------
	//Use of malloc and multiple pointers are referenced at top of program
	
	//Allocates memory for the 1st dimension of the 2d array
	new_grid = malloc(sizeof(int *)*num);
	
	//For loop to allocate memory for the 2nd dimension of the 2d array
	for(int i = 0; i < num; i++)
	{
		new_grid[i] = malloc(sizeof(int *)*num);
	}
	
	//Nested for loop to set all values in 2d array to 0
	for(int i = 0; i < num; i++)
	{
		for(int j = 0; j < num; j++)
		{
			new_grid[i][j] = 0;
		}
	}
	
	//Returns the 2d array to main
	return new_grid;
}

//Function that generates a array for the walls of the grid
int _Create_Walls_(int num, int ** Grid)
{
	//Local Decelerations----------------------------------
	int Determine_Wall; //Contains randomly generated 1 or 0 to determine
	int Pick_Wall;      //Stores random number between from 0 to 3
	
	//Local Statements-------------------------------------
	
	//Nested for loops to generate walls at each vertex
	for(int a = 0; a < num; a++)
	{
		for(int b = 0; b < num; b++)
		{
			//Randomly generated 1 or 0 declared to Determine_Wall
			Determine_Wall = rand() % 2;
					
			//Stores value of Determine_Wall in 3d array New_Walls 
			Grid[a][b] = Determine_Wall;
					
				
			//If statements to create exterior wall of grid.
			if(a == 0)
			{
				//Creates forward exterior wall
				Grid[a][b] = 1;
			}
				
			if(a == num - 1)
			{
				//Creates downward exterior wall
				Grid[a][b] = 1;
			}
				
			if(b == 0)
			{
				//Creates left side exterior wall
				Grid[a][b] = 1;
			}
				
			if(b == num - 1)
			{
				//Creates the right side exterior wall
				Grid[a][b] = 1;
			}
			
			//If statement to prevent start point from being a wall
			if(Grid[1][1] == 1);
			{
				Grid[1][1] = 0;
			}
			
			//If statement to prevent end point from being a wall
			if(Grid[num - 2][num - 2] == 1)
			{
				Grid[num - 2][num - 2] = 0;
			}
			

		}
		
	}
	
	//Nested for loop to go through all vertexes to create more possible paths
	for(int a = 0; a < num; a++)
	{
		for(int b = 0; b < num; b++)
		{
			//Nested if statements to possibly allow more paths in the maze by
			//removing walls
			if(Grid[a][b] == 1)						
			{						
				if(a - 1 >= 0)
				{
					if(a + 1 < num)
					{
						if(b - 1 >= 0)
						{
							if(b + 1 < num)
							{ 
								if(Grid[a-1][b] == 1)
								{
									if(Grid[a+1][b+1] == 1)
									{
										Grid[a][b] = 0;
									}
					
								}
							}
						}
					}
				}
			}
			
			
		}
	}
	

	//Returns the new array to main
	return Grid;			
}

int _Depth_First_Search_Traversal_ (int ** Grid, int num)
{
	//Local Decelerations----------------------------------
	int X_Coord, Y_Coord; //Variables to store vertex
	int pass = 1; //Variable to only allow _Depth_First_Search_ to run once.
	
	//Local Statements-------------------------------------
	X_Coord = 1;
	Y_Coord = 1;
	
	//If statement to see if a vertex is visited
	if(Grid[X_Coord][Y_Coord] == 0)
	{
		//Function call to determine if near nodes are visited
		_Depth_First_Search_(Grid, X_Coord, Y_Coord, num);
	}
		
	
	return Grid;
}

void _Depth_First_Search_(int ** Grid, int X_Coord, int Y_Coord, int num)
{
	//Local Decelerations----------------------------------

	//Local Statements-------------------------------------
	
	//If statement to stop DFS when a solution is found
	if(Grid[num - 2][num - 2] != 2)
	{	
		//Sets current vertex to visited
		Grid[X_Coord][Y_Coord] = 2;

		//Nested If statements to determine which direction to traverse
		//Traversal will not start if the current vertex is a wall 
		if(Grid[X_Coord + 1][Y_Coord] == 0)
		{
			
			//Increments X_Coord to move along the edge
			X_Coord++;
				
			//Performs _Depth_First_Search_ on new vertex
			_Depth_First_Search_(Grid, X_Coord, Y_Coord, num);
			
		}

		if(Grid[X_Coord][Y_Coord - 1] == 0)
		{
					
			//Decrements Y_Coord to move along the edge
			Y_Coord--;
					
			//Performs _Depth_First_Search_ on new vertex
			_Depth_First_Search_(Grid, X_Coord, Y_Coord, num);
					
		}
			
		if(Grid[X_Coord][Y_Coord + 1] == 0)
		{
				
			//Increments Y_Coord to move along the edge
			Y_Coord++;
				
			//Performs _Depth_First_Search_ on new vertex
			_Depth_First_Search_(Grid, X_Coord, Y_Coord, num);
				
				
		}
		
		if(Grid[X_Coord - 1][Y_Coord] == 0)
		{
			//Decrements X_Coord to move along the edge
			X_Coord--;
					
			//Performs _Depth_First_Search_ on new vertex
			_Depth_First_Search_(Grid, X_Coord, Y_Coord, num);
		}
					
						
	}
	
}
//Function to write HTML file and program output
void _Display_Maze_(int ** Grid, int num, int Maze_Counter)
{
	//Local Decelerations----------------------------------
	//NONE
	
	//Information to write HTML files and HTML information
	//is stated in the references at top of program
	
	FILE * fpointer; //Stores strings to write HTML file
	
	//Local Statements-------------------------------------
	//Opens/creates HTML file
	fpointer = fopen("Powell_MazeOutput_v1.06.html", "w");
	
	
	//fprintf statements to write HTML file to display maze 
	//header and information
	fprintf(fpointer, "<!DOCTYPE html>\n\n<html>\n");
	
	fprintf(fpointer, "	<head>\n	</head>\n");
	
	fprintf(fpointer, "	<body>\n		<!-- Program Output Information-->\n");
	
	fprintf(fpointer, "		<h1>Dustin Powell's Randomly Generated Maze and Path</h1>\n");
	
	fprintf(fpointer, "		<h2>Path = Blue, Unvisited Vertex = White, Visited Vertex = Red/Blue, Wall = Black</h2>\n");
	
	fprintf(fpointer, "		<h2>The maze size is: %d x %d </h2>\n", num, num);
	
	fprintf(fpointer, "		<table>\n");
	
	//Nested for loops to loop though values in 2d array Grid
	for(int i = 0; i < num; i++)
	{
		fprintf(fpointer, "			<tr>\n");
		
		for(int j = 0; j < num; j++)
		{
			//Nested if statements to determine which colored block to be displayed
			//in HTML
			if(Grid[i][j] == 1)
			{
				fprintf(fpointer, "				<td style=background-color:black height='15' width='15'></td>\n");
			}
			else
			{
				if(Grid[i][j] == 2)
				{
					fprintf(fpointer, "				<td style=background-color:red height='15' width='15'></td>\n");
				}
				else
				{
					if(Grid[i][j] == 0)
					{
						fprintf(fpointer, "				<td style=background-color:white height='15' width='15'></td>\n");
					}
					else
					{
						if(Grid[i][j] == 3)
						{
							fprintf(fpointer, "				<td style=background-color:blue height='15' width='15'></td>\n");
						}
					}
				}
			}
			
			
		}
		
		fprintf(fpointer, "			</tr>\n");
		
	}
	
	//fprintf statements to write number of maze loops
	fprintf(fpointer,"Number of loops during generation: %d", Maze_Counter);
	
	//fprintf statements to finish HTML file
	
	fprintf(fpointer, "		</table>\n");
	
	fprintf(fpointer, "\n	</body>\n</html>");
	
	//Closes HTML file
	fclose(fpointer);
	
	
}

//Function to create a path from start point to finish of maze
//The function comes from use in previous version of program
int _Create_Path_(int ** Grid, int X_Coord, int Y_Coord, int num)
{
	//Local Decelerations----------------------------------

	//Local Statements-------------------------------------

	//If statement to back track maze when a solution is found
	if(Grid[num - 2][num - 2] != 3)
	{	

		//Sets current vertex to visited
		Grid[X_Coord][Y_Coord] = 3;

		//Nested If statements to determine which direction to traverse
		//Traversal will not start if the current vertex is a wall 
		if(Grid[X_Coord][Y_Coord + 1] == 2)
		{
				
			//Increments X_Coord to move along the edge
			Y_Coord++;
			
			//Performs _Create_Path_ on new vertex
			_Create_Path_(Grid, X_Coord, Y_Coord, num);
				
		}
		else 
		{
			if(Grid[X_Coord + 1][Y_Coord] == 2)
			{
				//Increments Y_Coord to move along the edge
				X_Coord++;
				
				//Performs _Create_Path_ on new vertex
				_Create_Path_(Grid, X_Coord, Y_Coord, num);
			}
			else 
			{
				
				if(Grid[X_Coord][Y_Coord - 1] == 2)
				{
					//Decrements Y_Coord to move along the edge
					Y_Coord--;
					
					//Performs _Create_Path_ on new vertex
					_Create_Path_(Grid, X_Coord, Y_Coord, num);
				}
				else
				{
					
					if(Grid[X_Coord - 1][Y_Coord] == 2)
					{
						//Decrements X_Coord to move along the edge
						X_Coord--;
					
						//Performs _Create_Path_ on new vertex
						_Create_Path_(Grid, X_Coord, Y_Coord, num);
					}
				
				}
				
			}
			
		}		
	}
	
	return Grid;
}

