n = list(map(int,input().split()))
flag = False
max_step=0;
for i in range(len(n)):
    if(i < len(n) and i <= max_step):
        max_step = max( i + n[i], max_step);
        if(i == len(n)-1):
            flag = True
if(flag == True):
    print(1)
else:
    print(0)