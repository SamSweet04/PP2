new_file = open("new.txt","w")
mylist = input().split()
for i in mylist:
    new_file.write(i + " ")
