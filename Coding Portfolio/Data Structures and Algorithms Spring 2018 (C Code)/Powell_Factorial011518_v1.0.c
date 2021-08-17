//Program: Powell_Factorial011518_v1.0.c
//Due Date: 01/15/2018
//Author: Dustin Powell
//Objective: Create a program to determine the largest number of n! 
//and the amount of time it takes

//Honor Code: On my honor, I have neither given nor recived unauthorized or 
//unacknowledged aid on this academic work and I am unaware of any violations 
//of this code by others.
//Signed: Dustin Powell

//Acknowledgement Notes:
//Time functions come from website below:
//https://www.tutorialspoint.com/c_standard_library/c_function_difftime.htm
//Concept of fractionals come from below link:
//http://mathworld.wolfram.com/Factorial.html

//Change Log-------------------------------------------------------------------
//v1.0 01/15/18
//-first complete version of program

//Largest number output:
//2076180480

//Libaries---------------------------------------------------------------------
#include <stdio.h>
#include <time.h>

//Data Type Declerations-------------------------------------------------------
typedef unsigned long long undl;  //Unsigned long long defined as undl instead

//Function Decleartions--------------------------------------------------------
void _find_factorial_(undl n_factorial, undl input);

int main(int argc, char *argv[])
{
	//Local Declerations-----------------------------------
	undl n_factorial = 1;  //Number outputed from n! set to one for first n!
	undl input;            //User inputed number n 
	
	time_t start_clock, stop_clock;  //Varribles that store the start 
	                                 //and stop times for timer.
	double time_passed;              //Varriable of time passed since start of
	                                 //calculations.

	//Local statments--------------------------------------
	
	input = atoi(argv[1]);           //Converts command line input from string 
	                                 //to interger.
	
	time(&start_clock);              //Stores 1st time in a varrible

	_find_factorial_(input, n_factorial); //Function to calculate n!
	
	time(&stop_clock);               //Stores 2nd time in a varrible
	
	time_passed = difftime(stop_clock, start_clock); //Libary function that 
	//calculates and stores the time elpased between the two times
	
	//Prints time that took  for n! to be calculated
	printf("\nTime taken to calculate: %f", time_passed); 
	          
}
//Functions--------------------------------------------------------------------
void _find_factorial_(undl n_factorial, undl input) //Function to calculate n!
{
	while(n_factorial > 0)   //Loop to calculate n! factorial
	{
		n_factorial = n_factorial * input; //calculates the factorial 
		
		if(n_factorial > 0) //if statment is to prevent negative integers
		{
			printf("\n\n%d! is: %d", input, n_factorial); //prints computation
		}
		
		input++;    //Increments the input by one to compute next factorial
	}
	
}