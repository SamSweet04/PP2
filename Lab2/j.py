n = int(input())
l = []
for i in range(n):
    up,low,dig = False,False,False
    s = input()
    for j in range(len(s)):
        if(s[j].isupper()):
            up = True
            break
    for j in range(len(s)):
        if(s[j].islower()):
            low = True
            break
    for j in range(len(s)):
        if(s[j].isdigit()):
            dig = True
    if(up==True and low==True and dig==True):
        l.append(s)
l = list(set(l))    
print(len(l))
for i in sorted(l):
    print(i)


    
