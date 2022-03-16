import os
my_url = os.getcwd()
if os.access(my_url, os.F_OK): #checking the existence of a file or directory
    print("Yes,exist")
else: print("No,doesn't exist")
if os.access(my_url, os.R_OK): #checking the readability
    print("Yes,readable")
else: print("No,doesn't readable")
if os.access(my_url, os.W_OK): #checking the writability
    print("Yes,writable")
else: print("No,doesn't writable")
if os.access(my_url, os.X_OK): #checking file execution or directory opening
    print("Yes,executable")
else: print("No,doesn't executable")