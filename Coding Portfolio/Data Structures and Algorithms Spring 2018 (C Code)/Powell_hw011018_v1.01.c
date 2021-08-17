//Program: Powell_hw011518_v1.01.c
//Due Date: 01/15/2018
//Author: Dustin Powell
//Objective: Create a recurvsive function to add numbers, and also to
//count the number of calls, time, and operations per function. 

//Honor Code: On my honor, I have neither given nor recived unauthorized or 
//unacknowledged aid on this academic work and I am unaware 
//of any violations of this code by others.
//Signed: Dustin Powell

//Acknowledgement Notes:-------------------------------------------------------
//Mathmatical formula used for mathmatical sum is derived from 
//Sigma Notation which was learned in Calculus 1.
//Timer useage comes from link below:
//https://www.tutorialspoint.com/c_standard_library/c_function_difftime.htm

//Change Log-------------------------------------------------------------------
//v1.00 01/10/18
//- first program version
//v1.01 01/15/18
//- added change log with previous version notes
//- added sperate function for mathmatical function
//- added command line input & string to interger conversion for input
//- added operation counters
//- added libary time.h
//- added call counter to all functions
//- removed user prompt for input via printf
//- moved sumPrint and recurve varriable values to local declarations in main
//- updated function names to contain underscores
//- updated the comments in the program
//- seperated mathmatical function sum into own function
//- updated the objective of program
//-----------------------------------------------------------------------------

//Libaries---------------------------------------------------------------------
#include <stdio.h>
#include <time.h>

//Function Declerations--------------------------------------------------------

//Function to find mutiple sums from 1 to user inputed interger "n"
int _recurvsive_Fnc_(int n, int recurve, int sum_Print, int call_Count_one);

//Function to find sum using mathmatical function learned in calculus 1                                             
int _sigma_Fnc(int n, int call_Count_two);
											 
//Main Function----------------------------------------------------------------									 
int main (int argc, char *argv[])
{
	//Local Declerations-----------------------------------
	int n;                 //Command line inputed number
	int recurve = 1;       //Determine if a function is able to recurve
	int sum_Print = 1;     //Determines if a function is able to print first sum 
	int call_Count_one;             //Stores _recursive_Fnc_ number of calls
	int call_Count_two;             //Stores _sigma_Fnc_ number of calls
	int total_call_Count;           //Stores total number of calls
	time_t total_start, total_stop; //Stores computation start and stop times
	time_t sigma_start, sigma_stop; //Stores _sigma_Fnc_ start and stop times
	double total_time_passed;       //Stores total time passed computeing sums
	double sigma_time_passed;       //Stores times passed for _sigma_Fnc_
	
	//Command Line Input conversion to Interger
	n = atoi(argv[1]);
	
	//Locals Statments-------------------------------------
	
	time(&total_start);                     //Stores start time of computions
	
	//Function call to add sum from numbers 1 to user number and returns number of calls
	call_Count_one = _recurvsive_Fnc_(n, recurve, sum_Print, call_Count_one);

	time(&sigma_start);  	//Stores start time of _sigma_Fnc_
	
	//Matmatcial function sum call and returns number of calls
	call_Count_two = _sigma_Fnc(n, call_Count_two);  
	
	time(&sigma_stop);                     //Stores end time of _sigma_Fnc_
	
	//Stores and computes time taken to compute _sigma_Fnc_
	sigma_time_passed = difftime(sigma_stop, sigma_start); 
	
	//Outputs the time taken of mathmatical function
	printf("The time taken to compute mathmatical function sum: %f seconds\n\n", sigma_time_passed);
	
	time(&total_stop);                     //Stores stop time of computations
	
	//Stores and computes time taken to compute all sums
	total_time_passed = difftime(total_stop, total_start);
	
	//Outputs time taken to compute all sums
	printf("The time taken to compute all sums: %f seconds\n", total_time_passed);
	
	//Calcualtes total number of calls from each function
	total_call_Count = call_Count_one + call_Count_two;
	
	//Outputs number of functions called
	printf("The number of functions called is: %d", total_call_Count);
	
}

//Functions--------------------------------------------------------------------

//Function to count from 1 to "n"
int _recurvsive_Fnc_(int n, int recurve, int sum_Print, int call_Count_one)  
{
	//Local Declerations-----------------------------------
	int sum;                        //Calculated sum of numbers from 1 to "n"
	int add;                        //Increment for the for loop and adding sum
	int operations = 0;             //Varible stores number of operations 
	time_t start, stop;             //Variable used to store time 
	double time_passed;             //Variable stores time passed between to times
	
	//Local Statments--------------------------------------
	
	call_Count_one++;               //Increment to detemine number of function calls
	
	time(&start);                   //stores time in varrible start
	
	for(add = 1; add <= n; add++)   //Loop to add sum from 1 to "n"
	{
		sum = sum + add;            //Loop formula
		operations++;               //Increment for number of operations
	}
	
	time(&stop);                    //stores a second time in varrible stop
	
	//function determines amount of time between to times
	time_passed = difftime(stop, start); 
	
	//If statment to only allow print statement to run once
	if(sum_Print == 1)        
	{
		//Outputs first sum from 1 to "n"
		printf("The sum from 1 to N is: %d\n", sum);
		//Outputs number of operations for first sum
		printf("The number of operations used for first sum is: %d\n", operations); 
		//Outputs time taken to compute sum
		printf("The time taken to compute sum: %f seconds\n\n", time_passed);
	}
	
	//If statment to only allow _recurvsive_Fnc_ to recurve once
	if(recurve == 1)        
	{
		//_recurvsive_Fnc_ call with changed values to prevent 
		//duplicating print statments and recurveing more than once.
		_recurvsive_Fnc_(n, 0, 0, call_Count_one);
	}                  
	else
	{
		
		//Outputs sum of the recursive sum
		printf("The recursive sum from 1 to N is: %d\n", sum);
		
		//Outputs number of operations for recursive sum
		printf("The number of operations for recursive is: %d\n", operations);
		
		//Outputs time taken to compute recursvie sum
		printf("The time taken to compute recursive sum: %f seconds\n\n", time_passed);
	}
	call_Count_one++;             //Second increment to determine number of function calls
	
	return call_Count_one;
}

//Function that calculates 1 to n with sigma function
int _sigma_Fnc(int n, int call_Count_two)    
{
	//Local Declerations-----------------------------------
	int function_Sum;  //Calculated sum using mathamical function
	int operations;    //Varrible stores number of operations in equation
	
	//Local Statments--------------------------------------
	call_Count_two++;      //Increment to determine number of fucntion calls
	
	//Function derived from Sigma Notation learned in calculus 1
	function_Sum = (n*(n+1))/2; 
	operations = 3;             //Number of operations by function
	
	//Print statment outputs sum of mathmatical formula	
	printf("The mathmatical function from 1 to N is: %d\n", function_Sum);
	                   
	//Print statment outputs number of operations for mathmatical formula 					
	printf("The number of operations for mathmatical function is: %d\n", operations);
	
	return call_Count_two;                  
}


