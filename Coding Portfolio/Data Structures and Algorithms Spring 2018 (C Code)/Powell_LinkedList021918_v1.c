//Program: Powell_LinkedList021918_v1
//Due Date: 02/15/2018
//Author: Dustin Powell
//Objective: Create functions  discussed in class to edit an array 
//such as insert, remove, and sort.

//Honor Code: On my honor, I have neither given nor received unauthorized or 
//unacknowledged aid on this academic work and I am unaware of any violations 
//of this code by others.
//Signed: Dustin Powell

//Acknowledgment Notes:
//Library information and functions:
//https://www.tutorialspoint.com/c_standard_library/index.htm
//Functions used come from in class discussion


//Change Log-------------------------------------------------------------------
//v1 02/19/18
//-first complete version of program

//Compiler Used----------------------------------------------------------------
//gcc -o Powell_LinkedList021918_v1 Powell_LinkedList021918_v1.c

//Output ----------------------------------------------------------------------
/*
----------02/19/18 Version 1--------------
Powell_LinkedList021918_v1 5
           Starting Array
-----------------------------------
Index: 0        Value: 1
Index: 1        Value: 2
Index: 2        Value: 3
Index: 3        Value: 4
Index: 4        Value: 5
Index: 5        Value: 6
Index: 6        Value: 7
Index: 7        Value: 8
Index: 8        Value: 9
Index: 9        Value: 10
Index: 10       Value: 11
Index: 11       Value: 12
Index: 12       Value: 13
Index: 13       Value: 14
Index: 14       Value: 15
Index: 15       Value: 16
Index: 16       Value: 17
Index: 17       Value: 18
Index: 18       Value: 19
Index: 19       Value: 20

      Edits to the Array
-----------------------------------

Inserting 'n' index into Array
The new value inserted at index 5 is 5

Appending the array with value 'n'
New value appended is at index 21 is 5

Removing 'n' index from Array
The new value at index 5 is now 6

Reversing the elements of the Array

Searching the Array for the 'n' element in the array
The element 5 is located at index 0

Sorting the Array from least to greatest

Popping the Array
Popping the head of the array element 1

Extending the Array by 'n' elements

Counter the elements in Array
The array contains 26 elements

        Results from Edits
-----------------------------------
Index: 0        Value: 5
Index: 1        Value: 2
Index: 2        Value: 3
Index: 3        Value: 4
Index: 4        Value: 5
Index: 5        Value: 6
Index: 6        Value: 7
Index: 7        Value: 8
Index: 8        Value: 9
Index: 9        Value: 10
Index: 10       Value: 11
Index: 11       Value: 12
Index: 12       Value: 13
Index: 13       Value: 14
Index: 14       Value: 15
Index: 15       Value: 16
Index: 16       Value: 17
Index: 17       Value: 18
Index: 18       Value: 19
Index: 19       Value: 20
Index: 20       Value: 6487376
Index: 21       Value: 6487376
Index: 22       Value: 6487376
Index: 23       Value: 18
Index: 24       Value: -1
Index: 25       Value: 20

----KNOWN ERRORS IN CODE-----

After _Append_Array_ 'n' is no longer declared and has to be redeclared.

After _Reverse_Array_ 'n' is no longer declared and has to be redeclared.

The back to back usage of the functions causes the functions to not perform
properly such as _Search_Array_ and _Sort_Array_ when performed independently
each perform as as they should.

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
int MAX = 19; //Determines number of elements in array array[]
//Global Constants-------------------------------------------------------------


//Function Declarations--------------------------------------------------------

//_Insert_Array_ insert element 'n' at index 'n'
void _Insert_Array_(int *array[], int n);

//_Append_Array_ inserts element 'n' at the end of the array
void _Append_Array_(int *array[], int n);

//_Remove_From_Array_ removes 'n' index element from the array
void _Remove_From_Array_(int *array[], int n);

//_Reverse_Array_ reverses the elements of the array
void _Reverse_Array_(int *array[]);

//_Search_Array_ searches the array for what index an element is at
void _Search_Array_(int array[], int n);

//_Extend_Array_ adds 'n' indexes to the array
void _Extend_Array_(int *array[], int n);

//_Sort_Array_ sorts the array elements from least to greatest value
void _Sort_Array_(int *array[]);

//_Count_Array_ counts the number of elements in the array
void _Count_Array_(int array[]);

//_Pop_Array_ pops the first element of the array
void _Pop_Array_(int *array[]);

//Main-------------------------------------------------------------------------
int main(int argc, char *argv[])
{
	
	//Local Decelerations-----------------------------------
	int n;            //User inputed number n at the command line
	int number = 1;   //Variable to store starting number value in the array
	int *array[MAX];  //Array of integers from 1 to MAX elements


	//Local Statements-------------------------------------
	n = atoi(argv[1]); //Coverts command line input to integer.
	
	//Header for initial array before edits
	printf("           Starting Array\n");
	printf("-----------------------------------\n");
	
	//For loop to generate numbers and declare the numbers in the array
	//also to print the initial starting array
	for(int i = 0; i <= MAX; i++)
	{
		//Declares value to array[i]
		array[i] = number;
		
		//Prints the current value at array[i]
		printf("Index: %d\tValue: %d\n", i, array[i]);
		
		//Increments variable number
		number++;
	}
	
	//Header for the list of edits to the array
	printf("\n      Edits to the Array\n");
	printf("-----------------------------------\n");
	
	//Function call to _Insert_Array_ and passes by reference array[] 
	_Insert_Array_(&array, n);
	
	//Function call to _Append_Array_ and passes by reference array[]
	_Append_Array_(&array, n);
	
	
	//Redeclares the value of 'n' because of memory allocation 
	n = atoi(argv[1]);
	
	//Function call to _Remove_From_Array_ and passes by reference array[]
	_Remove_From_Array_(&array, n);
	
	//Function call to _Reverse_Array_ and passes by reference array[]
	_Reverse_Array_(&array);
	
	//Redeclares the value of 'n' because of memory allocation 
	n = atoi(argv[1]);
	
	//Function call _Search_Array_ searches the array for what index an element is at
	_Search_Array_(array, n);

	//Function call to _Sort_Array_ and passes by reference array[]
	_Sort_Array_(&array);
	
	//Function call to _Pop_Array_ and passes by reference array[]
	_Pop_Array_(&array);
	
	//Function call to _Extend_Array_ and passes by reference array[]
	_Extend_Array_(&array, n);
	
	//Function call _Count_Array_ counts the number of elements in the array
	_Count_Array_(array);
	
	//Header for the list of edits to the array
	printf("\n        Results from Edits\n");
	printf("-----------------------------------\n");
	
	//For loop to print out the array after edits
	for(int i = 0; i <= MAX; i++)
	{
		
		printf("Index: %d\tValue: %d\n", i, array[i]);
		
	}
}
//Functions--------------------------------------------------------------------

//Function _Insert_Array_ insert element 'n' at index 'n'
void _Insert_Array_(int *array[], int n)
{
	//Local Decelerations-----------------------------------
	int i;     //Stores the value of the max elements in array before shifting
	int shift; //Variable used to store element that is being shifted by one
	
	//Local Statements-------------------------------------
	//Prints the function being performed
	printf("\nInserting 'n' index into Array\n");
	
	//Stores the initial max variable in i before inserting new element
	i = MAX;
	
	//Increases the number of elements in the array by one
	MAX++;
	
	//For loop to shift values in the array to allow for new element
	for(i; n <= i; i--)
	{
		//Stores value of array[i] in variable shift
		shift = array[i];
		
		//Increments i to shift element forward one index
		i++;
		
		//Declares shifted value to new location at array[i]
		array[i] = shift;
		
		//Decrement to allow the next element to be shifted properly
		i--;
	
	}
	
	//Inserts the 'n' element at 'n' index after shifting
	array[n] = n;
	
	//Prints the value and index of the element
	printf("The new value inserted at index %d is %d\n", n, array[n]);
	
	return;
}

//Function _Append_Array_ inserts element 'n' at the end of the array
void _Append_Array_(int *array[], int n)
{
	//Local Decelerations-----------------------------------
	//NONE
	
	//Local Statements-------------------------------------
	
	//Prints the function being performed
	printf("\nAppending the array with value 'n'\n");
	
	//Increments the max elements by one
	MAX++;
	
	//Inserts new element at the end of the array
	array[MAX] = n;
	
	//Prints the value and index of the element added to the array
	printf("New value appended is at index %d is %d\n",MAX ,array[MAX]);
	
	
	return;
}

//Function _Remove_From_Array_ removes 'n' index element from the array
void _Remove_From_Array_(int *array[], int n)
{
	//Local Decelerations-----------------------------------
	int shift;   //Stores the element to be shifted in the array
	
	//Local Statements-------------------------------------
	//Prints the function being performed
	printf("\nRemoving 'n' index from Array\n");
	
	//For loop to shift the array backward to remove the element at 'n' index
	for(int i = n; i <= MAX; i++)
	{
		//Increments i forward one index
		i++;
		
		//Stores the element of array[i] in shift
		shift = array[i];
		
		//Decrements i backward one index to allow for the element to be shifted
		i--;
		//Stores the element in shift in array[i]
		array[i] = shift;
		
	}
	
	//Decrements MAX to remove last element in array
	MAX--;
	
	//Prints the new element and the index of the array
	printf("The new value at index %d is now %d\n", n, array[n]);
	
	return;
}

//Function _Reverse_Array_ reverses the elements of the array
void _Reverse_Array_(int *array[])
{
	//Local Decelerations-----------------------------------
	int j = MAX; 
	int value_1;   //Stores the first value to be flipped
	int value_2;   //Stores the second value to be flipped
	int half_MAX;  //Stores the value of half of the MAX elements
	
	//Local Statements-------------------------------------
	//Prints the function being performed
	printf("\nReversing the elements of the Array\n");
	
	//MAX number of elements divided by two determines the number of loops performed.
	half_MAX = MAX / 2;
	
	//For loop to flip the elements in the array
	for(int i = 0; i < half_MAX; i++)
	{
		//Stores the value at array[i] in value_1
		value_1 = array[i];
		
		//Stores the value at array[j] in value_2
		value_2 = array[j];
		
		//Flip occurs by storing value_2 in array[i]
		//and value_1 in array[j]
		array[i] = value_2;
		
		array[j] = value_1;
		
		//Decrements from MAX number of elements to half the number of elements 
		j--;
	}
	
	return;
}

//Function _Search_Array_ searches the array for what index an element is at
void _Search_Array_(int array[], int n)
{
	//Local Decelerations-----------------------------------
	//NONE
	
	//Local Statements-------------------------------------
	//Prints the function being performed
	printf("\nSearching the Array for the 'n' element in the array\n");
	
	//Loop to search the index of 'n' element
	for(int i = 0; i <= MAX; i++)
	{
		//if statement to determine if array[i] has 'n' element stored
		if(array[i] == n)
		{
			//Prints out the index of 'n' element
			printf("The element %d is located at index %d\n", array[i], i );
		}
		
	}
	
	return;
}

//Function _Extend_Array_ adds 'n' indexes to the array
void _Extend_Array_(int *array[], int n)
{
	//Local Decelerations-----------------------------------
	//NONE
	
	//Local Statements-------------------------------------
	//Prints the function being performed
	printf("\nExtending the Array by 'n' elements\n");
	
	//Loop to increase the elements of the array by 'n'
	for(int i = 0; i <= n; i++)
	{
		//Increments the max number of elements by one
		MAX++;

	}
	
	return;
}

//_Sort_Array_ sorts the array elements from least to greatest value
void _Sort_Array_(int *array[])
{
	//Local Decelerations-----------------------------------
	int low;   //Stores smallest value element at array[i]
	int index; //Stores the index of the smallest value element at array[i]
	int value_2; //Stores the element of array[i] before array[i] is changed

	//Local Statements-------------------------------------
	//Prints the function being performed
	printf("\nSorting the Array from least to greatest\n");
	
	//For loop to store values to least to greatest
	for(int i = 0; i <= MAX; i++)
	{
		//For loop to determine smallest value able to be stored at
		//an index in array
		for(int j = 0; j <= MAX; j++)
		{
			//if statement to determine if a value is able to be store
			//at an index in the array
			if(array[i] >= array[j])
			{
				//Stores element at variable low 
				low = array[j];
				
				//Stores the index of array[j]
				index = j;
				
			}
			
		}
		
		//Stores the element of array[i] in value_2
		value_2 = array[i];
		
		//Stores the element in low in array[i]
		array[i] = low;
		
		//Stores value_2 at array index to be possibly moved later
		array[index] = value_2;
		
		
	}
	
}

//_Count_Array_ counts the number of elements in the array
void _Count_Array_(int array[])
{
	//Local Decelerations-----------------------------------
	int counter = 0;  //Variable to count the number of elements in the array
	
	//Local Statements-------------------------------------
	//Prints the function being performed
	printf("\nCounter the elements in Array\n");
	
	//For loop to count the number of elements in the array
	for(int i = 0; i <= MAX; i++)
	{
		//Counter increments by one each loop to represent an element
		counter++;
	}
	
	//Prints the number of elements in the array
	printf("The array contains %d elements\n", counter);
	
	return;
}

//_Pop_Array_ pops the first element of the array
void _Pop_Array_(int *array[])
{
	//Local Decelerations-----------------------------------
	int shift; //Store value of array[i] to be shifted 
	
	//Local Statements-------------------------------------
	//Prints the function being performed
	printf("\nPopping the Array\n");
	//Prints the element being popped from the array
	printf("Popping the head of the array element %d\n", array[0]);
	
	//For loop to shift elements backward in the array
	for(int i = 0; i <= MAX; i++)
	{
		//Increments i forward one index
		i++;
		
		//Stores the element of array[i] in shift
		shift = array[i];
		
		//Decrements i backward one index to allow for the element to be shifted
		i--;
		
		//Stores the element in shift in array[i]
		array[i] = shift;
		
	}
	
	//Decrements MAX to remove last element in array
	MAX--;
	
	return;
}


