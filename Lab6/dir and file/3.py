import os 
my_url = "C:\PP2\Lab6\dir and files\input.txt"
if os.access(my_url, os.F_OK):
    print(os.path.basename(my_url))
    print(os.path.dirname(my_url))
else: print("Not exists")