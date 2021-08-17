/* D=RT Program Written by: Dustin Powell 
Date: 9/26/2017 */

// declare rate, time, and distance as int
// distance = rate * time
// 110 miles = 55mph * 2 hours
// ask for user input of rate and time
// calculate user input
// output user calcualted data

// Question Answers: C. Changed the way the varribles were declared, No chang in output occured
/* Preprocessor directive to include header file stdio.h  */

#include <stdio.h>

//Function Declaration

int disCalc(int rate, int time);                                           //Distance Calculation function decleration

int main(void)
{
    /* Declaration of 3 varaibles with comments for each  */
    int rate, time;                                                         //Rate and time local decleration
	  
	
    /* Initialization of speed and time elapsed    */
	
	printf("Enter the rate in miles per hour and time in hours :");         //User prompt and data input
	scanf("%d %d", &rate, &time);
	
	
    /* Print values of 3 variables  */
	printf("Please read aloud the speed and time");                         //Prompts user to read aloud data vaules and calcualted distance
	printf("\nYour current rate is :%d mph", rate);
	printf("\nYour current time is :%d hours", time);
	printf("\nYour calcualted distance is: %d miles", disCalc(rate, time));
    
}

int disCalc(int rate, int time)                                             //Distance Calculation function
{	
	int distance;                                                             // Distance Variable
	
	distance = rate * time;                                                   // Distance equation
	
	return distance;
}
	