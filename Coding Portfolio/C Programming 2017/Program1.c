// Program Assignemnt 1: Payroll Calculation Program
// Made by Dusitn Powell
// Due Date:9/20/2017


#include <stdio.h>

// Function Declerations
float withSsTax(float ssTax, float grossPay);
float withFedTax(float fedTax, float grossPay);
float withStateTax(float stTax, float grossPay);
float withPremiums(float premiums);
float netPay(float grossPay, float ssPay, float fedPay, float statePay, float premiums);

// Information Input and Function Calls
int main(void)
{
	// Local Declerations
	
	float payRate;        //Pay Rate
	int   workHour;       //Hours Worked
	float ssTaxInt;       //Social Security Tax Rate not calculated
	float ssTax;          //Social Security Tax Rate calculated
	float fedTaxInt;      //Federal Income Tax Rate not calculated
	float fedTax;         //Federal Income Tax Rate calculated
	float stTaxInt;       //State Income Tax Rate not calculated
	float stTax;          //State Income Tax Rate calculated
	float premiums;       //Insurance premiums 
	float grossPay;       //Gross pay
	float ssPay;          //Social Security Tax Payment	
	float fedPay;         //Federal Income Tax Payment
	float statePay;       //State Income Tax Payment
	
	
	// Statement Program Header
	
	printf("\n                Payroll Calulation\n \n");
	
	// Statements Entering Data & Calculating Percentages
	
	printf("Enter pay rate: $");                                  //User prompt & input pay rate
	scanf("%f", &payRate);
	
	printf("Enter number of hours worked: ");                     //User prompt & input hours worked
	scanf("%d", &workHour);
	
	printf("Enter social secuirty tax rate: %%");                 //User prompt & input SSN Tax Rate & percentage calculation
	scanf("%f", &ssTaxInt);
	ssTax = ssTaxInt / 100.00;                                       //Converts to percentage 
	
	printf("Enter the federal income tax rate: %%");              //User prompt & input Fed Income Tax Rate & percentage calculation
	scanf("%f", &fedTaxInt);
	fedTax = fedTaxInt / 100.00;                                     //Converts to percentage
	
	printf("Enter the state income tax rate: %%");                //User prompt & input State Income Tax Rate & percentage calculation
	scanf("%f", &stTaxInt);
	stTax = stTaxInt / 100.00;                                       //Converts to percentage
	
	printf("Enter the additional fee for insurance premiums: $"); //User prompt & input insurance premiums
	scanf("%f", &premiums);
	
	// Payroll Information Header
	
	printf("\n\n\n ---Payroll Information---\n");
	
	// Calculation & Output Call Functions
	
	
	grossPay = workHour * payRate;	                             //Gross pay Caulation & output
    printf("Gross Pay: $%4.2f", grossPay);
	
	ssPay = withSsTax(ssTax, grossPay);                          //Social Secuity Tax Calculation & Ouput
	
	
	fedPay = withFedTax(fedTax, grossPay);                       //Federal Income Tax Calculation & Ouput
	
	
	statePay = withStateTax(stTax, grossPay);                    //State Income Tax Calculation & Ouput
	
	
	withPremiums(premiums);                                      //Insurance Premiums Ouput
	
	netPay(grossPay, ssPay, fedPay, statePay, premiums);         //Net pay Calculation & Output
	
	
}
// Withholding Social Secuirty 
float withSsTax(float ssTax, float grossPay)
{
	// Local Declerations
	float ssPay; 

	// Statements
	ssPay = ssTax * grossPay;
	printf("\nWithheld social secuirty tax: $%4.2f", ssPay);
	
	return ssPay;
}
// Withholding Federal Income Tax 
float withFedTax(float fedTax, float grossPay)
{
	// Local Declerations
	float fedPay;
	
	// Statements
	fedPay = fedTax * grossPay;
	printf("\nWithheld federal income tax: $%4.2f", fedPay);
	
	return fedPay;
}
// Withholding State Income Tax
float withStateTax(float stTax, float grossPay)
{
	// Local Declerations
	float statePay;
	
	// Statements
	statePay = stTax * grossPay;
	printf("\nWithheld state income tax: $%4.2f", statePay);
	
	return statePay;
}
// Insurance Premiums Payment
float withPremiums(float premiums)
{
	// Local Declerations
	
	// Statments
	printf("\nWithheld insurance premiums: $%4.2f", premiums);
	
	return;
}
// Net Pay
float netPay(float grossPay, float ssPay, float fedPay, float statePay, float premiums)
{
	// Local Declerations
	float netPay;
	
	// Statments
	netPay = grossPay - (ssPay + fedPay + statePay + premiums);
	printf("\nNet take-home pay for this pay period: $%4.2f", netPay);
	
	
}	