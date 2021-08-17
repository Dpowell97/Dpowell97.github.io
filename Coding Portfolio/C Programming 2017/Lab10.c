/*
 * Lab program to practice with arrays: printing, summing
 * incrementing and inserting.
 * Date: 11/21/17
 * Programmer: Dustin Powell
 *1a. Index 14 is initialized to 0 
 *
 */
#include <stdio.h>
#define MAX 20

void PrintArray(int b[], int NumEls);
int  SumArray(int b[],int NumEls);
void IncArray(int b[], int NumEls, int new);
int InsertArray(int a[], int NumEls, int new);

int main(void)
{
    int a[MAX] = {14,17,23,26,33,38,39,41,52,56};
	int NumEls;
    
    NumEls = 10;    /* number of elements in the array  */
    
    printf("Array at the start of the program: \n");
    PrintArray(a,NumEls);
    printf("\nThe sum of these elements is %d.\n\n",SumArray(a, NumEls));
	
    IncArray(a,10,5);
	
	printf("\nAfter Increment:\n");
    PrintArray(a,NumEls);
	printf("\nThe sum of these elements is %d. \n\n", SumArray(a, NumEls));
    
    /* Add statements to print out all the elements in the array and to sum the elements
     * in the array.
     */
    NumEls = InsertArray(a,NumEls,23);
    
    printf("\nAfter Insert: \n");
    PrintArray(a,NumEls);
    printf("\nThe sum of these elements is %d.\n\n", SumArray(a, NumEls));
    
    return 0;
}
/*
 * Function to print the first NumEls elements of array b
 * Pre:  b is an integer array.
 *       NumEls is the number of elements in b.
 * Post: The elements of b have been printed on a line
 *       sepearated by spaces.
 */
void PrintArray(int b[], int NumEls)
{
    int i;
    i = 14;
	printf("Array a has %d elements: ", NumEls);
	for(i = 0; i < NumEls; i++)
	{
	printf("%d ", b[i]);
	}
	
    //printf("\nThe element at index %d is %d.\n", i, b[i]);
}
/*
 * Function to return the sum of the first NumEls elements of array b
 */
int SumArray(int b[], int NumEls)
{
	int sum, i;
	
	for(i = 0; i < NumEls; i++)
	{
		if(i == 0)
		{
			sum = b[i];
		}
		else
		{
			sum = sum + b[i];
		}
	}
    return sum;
}

/*
 * Function to increment each element in array b by inc amount
 * Pre:  b is an integer array.
 *       NumEls is the number of elements in b.
 * Post: The elements of b have been incremented by inc
 *
 */
void IncArray(int b[], int NumEls, int new)
{
	int sum, i;
	
	for(i = 0; i < NumEls; i++)
	{
		b[i] += new;

	}
    return sum;
}
/*
 * Function to insert an element at the end of array b
 * Pre:  b is an integer array.
 *       NumEls is the number of elements in b.
 * Post: If array b is not at capacity, then the number x is
 *       added to the end of the array. NumEls is incremented and returned
 */
int InsertArray(int a[], int NumEls, int new)
{
	int i;
	i = NumEls;
	
	if(NumEls < MAX)
	{
		a[i] = new;
		++NumEls;
	}
	else
	{
		printf("The array is full");
	}
    return NumEls;
}