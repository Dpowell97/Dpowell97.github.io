//Program: Powell_Problem54012918_v1.0
//Due Date: 01/29/2018
//Author: Dustin Powell
//Objective: 

//Honor Code: On my honor, I have neither given nor recived unauthorized or 
//unacknowledged aid on this academic work and I am unaware of any violations 
//of this code by others.
//Signed: Dustin Powell

//Acknowledgement Notes:
//Libary information:
//https://www.tutorialspoint.com/c_standard_library/c_function_difftime.htm
//Prime Number functions and loops come from in class examples and problem 54 
//in book.

//Change Log-------------------------------------------------------------------
//v1.0 01/29/18
//-first complete version of program

//Output ----------------------------------------------------------------------
/*


 
 
 **errors: at i 17
 I did not know or could find proper code to output system specs but 
 system used to compute is:
 Processor:	AMD A10-8700P Radeon R6, 10 Compute Cores 4C+6G, 1800 Mhz, 
			2 Core(s), 4 Logical Processor(s)
		OS: OS Name	Microsoft Windows 10 Home
   Version: 10.0.16299 Build 16299
	   RAM: 8.00 GB



 
 
*/
//Libaries---------------------------------------------------------------------
#include <stdio.h>
#include <time.h>
#include <limits.h>
#include <math.h>
#include <stdlib.h>

//Data Type Declerations-------------------------------------------------------
typedef unsigned long long llu;

//Global Variables-------------------------------------------------------------
llu counter = 0; // Will be listed as counter++; throughout code.

//Function Decleartions--------------------------------------------------------
int Prime_Fnc_(llu num, llu prime_num); //Function to compute prime numbers.

int main(int argc, char *argv[])
{
	//Local Declerations-----------------------------------
	llu num;  //Number being tested by prime function.
	llu n;    //User input number of n primes wanted.
	llu prime_num; //Contains a prime number to be printed.
	time_t start, update, stop; //Time varribles.
	double time_pass;  //Time varrible in seconds stores differnece
	// between start and update or end times.

	//Local Statements-------------------------------------
	n = atoi(argv[1]); //Coverts command line input to interger.

	//Header for the output of categories.
	printf("    i    P    Counter    Time    ");
	printf("\n---------------------------------");
	  
	time(&start); //Start time stored in varrible start
	for(llu i = 1; i <= n; i++) //Loop to increment to user 'n' number and 
	{                           //determines value inputed to Prime_Fnc_.
		counter++;              //Increments operation count by 1.
		num = i;                //Varrible set to I to be manuiplate by Prime_Fnc_.
		if(i <= 3)              //If statment to account for 1 not being prime.
		{
			counter++;          //Increments operation count by 1.
			num++;              //Increments num by 1 to account for 1
		}                       //not being prime.
		
		prime_num = Prime_Fnc_(num, prime_num); //Call Prime_Fnc_ and outputed
		                                     //prime number stored in prime_num.
		time(&update);          //Time stored since start to determine time for
	                            //a prime number to be found.
		time_pass = difftime(update, start);//Calculates time taken to solve for
		                                    //a prime number.
		//Output of number i, prime number, # of operations, and time 
		//taken for the prime number.
		printf("\n    %llu    %llu       %llu       %f", i, prime_num, counter, time_pass);
	}
	time(&stop); //Stores stop time
	
	time_pass = difftime(stop, start);//Calculates total time taken 
									  //to solve for n primes
	
	printf("\n Total time taken = %f", time_pass); //Prints total time passed.
	
	
}

int Prime_Fnc_(llu num, llu prime_num)//Function to compute prime numbers.
{
	//Local Declerations-----------------------------------
	//NONE
	//Local Statements-------------------------------------
	if(num != 2)       //Removes numbers that are divided by the prime numbers
	{                  // 2, 3, 5, and 7 using modulus.
		if(num%2 == 0) // All contain counter++; to track number of operations.
		{
			counter++;
			num++;
		}
	}
	
	if(num != 3)
	{
		if(num%3 == 0)
		{
			counter++;
			num++;
		}
	}
	
	if(num != 5)
	{
		if(num%5 == 0)
		{
			counter++;
			num++;
		}
	}
	
	if(num != 7)
	{
		if(num%7 == 0)
		{
			counter++;
			num++;
		}
	}
		
	//Loop to find prime numbers stores in the varrible num
	for(llu j = 2; j <= sqrt(num); j++)//Code is from the book
	{                         //Increments j to sqrt(num)
		counter++;        //Operation counter increments by 1
		if(num%j == 0) //If statment that determines num is prime
		{
			counter++;
			num++;
			Prime_Fnc_(num, prime_num);
		}
		else if(num <= prime_num)//Else if statment to increment num if num
		{                        // equals last inputed prime.
			counter++;           //Operation counter increments by 1
			num++;               //Increments num by 1
			Prime_Fnc_(num, prime_num); //Calls the function to try to find 
		}                               //next prime number
		
		return;                  
	}
	
	return num;
}
	

	
