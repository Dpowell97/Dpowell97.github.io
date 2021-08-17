//Program: Powell_TowerOfHanoi020518_v1.01
//Due Date: 02/5/2018
//Author: Dustin Powell
//Objective: Find the number of moves per game of Tower of Hanoi
// for n number of games.

//Honor Code: On my honor, I have neither given nor received unauthorized or 
//unacknowledged aid on this academic work and I am unaware of any violations 
//of this code by others.
//Signed: Dustin Powell

//Acknowledgment Notes:
//Library information and functions:
//https://www.tutorialspoint.com/c_standard_library/c_function_difftime.htm
//_Tower_Solve_ come from the book and online to help fully understand the 
//function in book. Link below:
//https://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm
//In class examples and discussion topics were used to determine the 
//accuracy of the program.

//Other Notes:
//Algorithm located in _Solve_Tower_


//Change Log-------------------------------------------------------------------
//v1.0 02/5/18
//-first complete version of program
//v1.01 02/9/18
//- added printf statements to function _Solve_Tower_ 
//- updated change logs
//- updated compiler notes
//- added printf statments to algorithm in function _Tower_Solve_
//- added headers for each number of moves and data
//- removed headers from version 1.0

//Compiler Used----------------------------------------------------------------
//gcc -o Powell_TowerOfHanoi020518_v1.01 Powell_TowerOfHanoi020518_v1.01.c


//Output ----------------------------------------------------------------------
/*
-----Version 1.0 02/5/18------
Powell_TowerOfHanoi020518_v1.0 25

  Disk = i    Ops. Per game    Counter            Time
----------------------------------------------------------
  1:            1:              1:              0.000000 s
  2:            3:              4:              0.000000 s
  3:            7:              11:             0.000000 s
  4:            15:             26:             0.000000 s
  5:            31:             57:             0.000000 s
  6:            63:             120:            0.000000 s
  7:            127:            247:            0.000000 s
  8:            255:            502:            0.000000 s
  9:            511:            1013:           0.000000 s
  10:           1023:           2036:           0.000000 s
  11:           2047:           4083:           0.000000 s
  12:           4095:           8178:           0.000000 s
  13:           8191:           16369:          0.000000 s
  14:           16383:          32752:          0.000000 s
  15:           32767:          65519:          0.000000 s
  16:           65535:          131054:         0.000000 s
  17:           131071:         262125:         0.000000 s
  18:           262143:         524268:         0.000000 s
  19:           524287:         1048555:                0.000000 s
  20:           1048575:                2097130:                0.000000 s
  21:           2097151:                4194281:                0.000000 s
  22:           4194303:                8388584:                0.000000 s
  23:           8388607:                16777191:               1.000000 s
  24:           16777215:               33554406:               1.000000 s
  25:           33554431:               67108837:               1.000000 s
 Total time taken: 1.000000 s
 
 
 
 -----Version 1.01 02/7/18------
 
 Powell_TowerOfHanoi020518_v1.01 3


Disk = i: 1
        Moves
----------------------
Move disk 1 peg 1 to peg 3

     Game Data
----------------------
Number of operations in game: 1
Total completed operations: 1
Time taken to complete 0.000000 s

Disk = i: 2
        Moves
----------------------
Move disk 1 peg 1 to peg 2
Move disk 2 peg 1 to peg 3
Move disk 1 peg 2 to peg 1

     Game Data
----------------------
Number of operations in game: 3
Total completed operations: 4
Time taken to complete 0.000000 s

Disk = i: 3
        Moves
----------------------
Move disk 1 peg 1 to peg 3
Move disk 2 peg 1 to peg 2
Move disk 1 peg 3 to peg 1
Move disk 3 peg 1 to peg 3
Move disk 1 peg 2 to peg 3
Move disk 2 peg 2 to peg 1
Move disk 1 peg 3 to peg 2

     Game Data
----------------------
Number of operations in game: 7
Total completed operations: 11
Time taken to complete 0.000000 s

Total time taken: 0.000000 s


------------------------------------------------------------------------
 **Errors: After certain amount of lines, data begins to shift to the left 
 due to the size of the numbers being outputted. System information could not
 be printed out could not find a proper way to do so.
 
Specs for computer that gave the above output:
OS Name:	Microsoft Windows 10 Home
Version:	10.0.16299 Build 16299
Processor:	AMD Athlon(tm) X4 860K Quad Core Processor, 3700 Mhz, 
			2 Core(s), 4 Logical Processor(s)
Installed Physical Memory (RAM):	16.0 GB
Available Physical Memory:	11.9 GB


*/
//Libraries---------------------------------------------------------------------
#include <stdio.h>
#include <time.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>

//Data Type Decelerations------------------------------------------------------
typedef unsigned long long llu;

//Global Variables-------------------------------------------------------------
llu counter = 0; //Used to count number of operations performed overall.
llu Ops_Per_Game = 0; //Used to coun number of moves per game.
//Function Declarations--------------------------------------------------------
//Function to calculate number of moves per game and solves the Tower of Hanoi
int _Solve_Tower_(llu disk, llu Peg_One, llu Peg_Three);

int main(int argc, char *argv[])
{
	
	//Local Decelerations-----------------------------------
	llu n;         //User input number of games.
	llu disk;      //Stores number of disk per game increments by one each game
	llu Peg_One, Peg_Three;   //Stores the first and last peg number values.
	time_t start, update, stop; //Variables used to store time.
	double time_pass;  //Time variable in seconds stores difference
	//between start, update and end times.

	//Local Statements-------------------------------------
	n = atoi(argv[1]); //Coverts command line input to integer.
	
	
	time(&start);   //Stores a start time in variable start.
	
	//For loop to allow the game to run multiple times till 
	//n number of games is reached.
	for(int i = 1; i <= n; i++)
	{
		//I increments each loop and is declared to disk to determine number
		//of disk for each game.
		disk = i;
		printf("\n\nDisk = i: %llu", i);
		
		//Moves header
		printf("\n        Moves");
		printf("\n----------------------");
		
		//Calls function _Solve_Tower_ to determine the amount of moves per game.
		_Solve_Tower_(disk, 1, 3); 
		
		time(&update); //Stores a update time in variable update.
	
		//Calculates the difference between start time and update to determine
		//time taken per game.
		time_pass = difftime(update, start);
		
		//Game Data Header
		printf("\n\n     Game Data");
		printf("\n----------------------");
		
		//Data output for each game.
		
		printf("\nNumber of operations in game: %llu", Ops_Per_Game);
		printf("\nTotal completed operations: %llu", counter);
		printf("\nTime taken to complete %f s", time_pass);
		
		//Resets the number of operations in each game back to zero
		//to only count moves per game.
		Ops_Per_Game = 0;
		
		
	}
	
	//Stores a stop time in variable stop.
	time(&stop);
	
	//Calculates the difference between that start and stop time to determine 
	//the total time to play n games.
	time_pass = difftime(stop, start);
	
	//Outputs total time taken to play n games.
	printf("\n\nTotal time taken: %f s\n", time_pass);
}
//Functions--------------------------------------------------------------------

//Function to calculate number of moves per game and solve the Tower of Hanoi
int _Solve_Tower_(llu disk, llu Peg_One, llu Peg_Three)
{
	//Local Decelerations----------------------------------
	//NONE
	
	//Local Statements-------------------------------------
	counter++;//Counts the total amount of operations
	Ops_Per_Game++; //Increment to count number of moves per game.
	
	//Algorithm for Tower of Hanoi comes from book and online resource.
	//Further details in acknowledgment. 
	if(disk == 1)
	{
		//Printf statments comes from algorithm in book
		printf("\nMove disk %d peg %d to peg %d", disk, Peg_One, Peg_Three);
	}
	else
	{
		_Solve_Tower_(disk - 1, Peg_One, 6 - Peg_One - Peg_Three);
		
		//Printf statments comes from algorithm in book
		printf("\nMove disk %d peg %d to peg %d", disk, Peg_One, Peg_Three);
		
		_Solve_Tower_(disk - 1, 6 - Peg_One - Peg_Three, Peg_One);
	}
	
	
}	







