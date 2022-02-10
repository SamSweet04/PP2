a =int(input())
b = input()
if(b == 'b'):
    print(a*1024)
else:
    if b == 'k':
       print(round(a/1024,int(input())))
