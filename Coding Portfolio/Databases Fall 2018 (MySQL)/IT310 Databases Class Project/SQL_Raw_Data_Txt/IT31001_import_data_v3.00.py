"""
Program: IT31001_import_data_v3.00.py
Author: jvazquez88 [at] students.cumberland.edu

Description: The program reads the files in the list "files" and prints only
             the lines containing the data needed for the database, ignoring
             lines starting with the pound symbol ('#') or a newline ('\n').

References: -> Old homework that read and wrote files back from intro to
               programming.
            
"""
#-----------------------------------------------------------------------------80

import os

def main():

    files = ["CU_Trees_Table_TREE_Data_v1.00.txt",
             "CU_Trees_Table_TREE_INFO_Data_v1.00.txt",
             "CU_Trees_Table_TREE_TAXONOMY_Data_v1.00.txt",
             "CU_Trees_Table_TREE_USER_Data_v1.00.txt",
             "CU_Trees_Table_TREE_LOCATION_Data_v1.00.txt"]

    for i in files:
        print(i)
        to_open = open(i, 'r') 
        # if a line does nots tart with a # or a newline, it will print it.
        for j, line in enumerate(to_open):
            if line[0] != '#' and line[0] != '\n':
                print(line, end = '')
        to_open.close()
        print('\n')

main()
    
