a=list(map(int,input().split()))
new=[]
def prime(a):
  for i in range(len(a)):
    cnt=0
    for j in range(1,a[i]):
      if(a[i]%j==0):
        cnt+=1
    if(cnt==1):
     new.append(a[i])
  return new
print(*prime(a))