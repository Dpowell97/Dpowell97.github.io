//Program: PrimeNumbers
//Due Date: 02/19/2018
//Author: Dustin Powell


//Libraries--------------------------------------------------------------------
#include <stdio.h>
#include <math.h>
#include <limits.h>



//Data Type Decelerations------------------------------------------------------
typedef unsigned long long llu;



//Function Declarations--------------------------------------------------------

int main(int argc, char *argv[])
{
	//Local Decelerations----------------------------------
	llu n;
	
	//Local Statements-------------------------------------
	//Coverts command line input to integer.
	n = atoi(argv[1]);
	
	if (n > 1)
	{
		if (n == 2)
		{
			printf("%d is a prime number 1", n);
			
		}
		else
		{
			if( n % 2 == 0)
			{
				printf("%d is not prime 2", n);
			}
			else
			{

				
				for(int i = 1; i <= sqrt(n); i++)
				{
			
					if( i % n == 1)
					{
						printf("%d is prime 3", n );
						return;
					}
					else
					{
						printf("%d is not prime 4", n);
						return;
					}
					
				}
			}
					
				
				
		}
	}
	else
	{
		printf("%d is not prime", n);
	}
	
	
	
	
}