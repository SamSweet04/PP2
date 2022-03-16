import os
my_url = 'C:\PP2\Lab6\dir and files\deleted.txt' #link to delete the file
if os.access(my_url,os.F_OK):
    os.remove(my_url)
else:
    print("It doesn't exist!")