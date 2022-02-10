a,d= input(),input()
res = None
n = 0
for i in range(0,len(a)):
    if a[i] == d:
        res = i
        n+=1
if n >= 2:
    print(a.find(d), a.rfind(d),end="")
elif res == None:
    print("")
else:
    print(res)