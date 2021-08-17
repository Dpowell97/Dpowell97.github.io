"""
Program: IT101_Powell_ProjCH2_4_v1.00.py
Due Date: 09/13/18
Author: Dustin Powell

--------------------------------------------------------------------------------
Objective: Wrtie a program to output a sphere's diameter, circumference, surface
area, and volume using the radius.

--------------------------------------------------------------------------------
Project Algorithm:
1. Define the constants of the program.
2. Define the formulas and varribles of the program.
3. Prompt the user for input of the sphere's radius.
4. Calculate each measurement of the sphere based of the radius.
5. Output the results of each measurement.

--------------------------------------------------------------------------------
Honor Code: On my honor, I have neither given nor received unauthorized or 
unacknowledged aid on this academic work and I am unaware of any violations 
of this code by others.
Signed: Dustin Powell
--------------------------------------------------------------------------------
Acknowledgment Notes:
The website link below is were the sphere formulas were refered from:
https://formulas.tutorvista.com/math/sphere-formula.html
In class discussion and the course book were also used for syntax reference.

--------------------------------------------------------------------------------
Change Log:
-v1.00
    First complete version of the program.
--------------------------------------------------------------------------------
Compiler Used:
(Command Line on Ubuntu 18.04)

python3 IT101_Powell_ProjCH2_4_v1.00.py
--------------------------------------------------------------------------------
Output:
-v1.00
    Please enter the radius of the sphere: 52

    The diameter of the sphere is:  104.0 units
    The circumference of the sphere is:  326.56 units
    The surface area of the sphere is:  33962.24 units
    The volume of the sphere is:  11320.746666666666 units

--------------------------------------------------------------------------------
"""
#Libaries-----------------------------------------------------------------------
#NONE

#Global Constants---------------------------------------------------------------
PI = 3.14        #Global constant for Pi

#Main Function Decleration------------------------------------------------------
def main():

    #Local Declerations-------------------------------------
    sphere_Radius = 0.00         #Stores the user inputed sphere's radius.
    sphere_Diameter = 0.00       #Stores the calculated sphere's diameter.
    sphere_Circumference = 0.00  #Stores the calculated sphere's circumference.
    sphere_Surface_Area = 0.00   #Stores the calculated sphere's surface area.
    sphere_Volume = 0.00         #Stores the calcualted sphere's volume.

    #Local Statments----------------------------------------

    #Input function to prompt user for sphere's radius and stores the value
    sphere_Radius = float(input("Please enter the radius of the sphere: "))

    #Function call to calculate the sphere's diameter and stores the value
    sphere_Diameter = _calculate_diameter_(sphere_Radius)

    #Function call to calculate the sphere's circumference and stores the value
    sphere_Circumference = _calculate_circumference_(sphere_Radius)

    #Function call to calculate the sphere's surface area and stores the value
    sphere_Surface_Area = _calculate_surface_area_(sphere_Radius)

    #Function call to calculate the sphere's volume and stores the value
    sphere_Volume = _calculate_volume_(sphere_Radius)

    #Print statments to output the calculated measurements of the sphere
    print("\nThe diameter of the sphere is: ", sphere_Diameter, "units")
    print("The circumference of the sphere is: ", sphere_Circumference, "units")
    print("The surface area of the sphere is: ", sphere_Surface_Area, "units")
    print("The volume of the sphere is: ", sphere_Volume, "units")

#Function Declerations----------------------------------------------------------

#Function to calcualte the diameter of the sphere
def _calculate_diameter_(radius):
    
    return 2 * radius

#Function to calculate the circumference of the sphere
def _calculate_circumference_(radius):
    
    return 2 * PI * radius

#Function to calculate the surface area of the sphere
def _calculate_surface_area_(radius):

    return 4 * PI * (radius ** 2)

#Function to calculate the volume of the sphere
def _calculate_volume_(radius):

    return (4/3) * PI * (radius ** 2)

#Main Function Call-------------------------------------------------------------
main()
















