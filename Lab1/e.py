a,b= map(int, input().split())
flag = False
for i in range(2,a):
    if(a%i)==0:
        flag = True
        break
if flag == False and a<500 and b%2==0:
    print("Good job!")
else:
    print("Try next time!")