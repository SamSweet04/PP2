n = int(input())
demons = {}
sum = 0
for i in range(n):
    demons_name,weak = input().split()
    if weak not in demons:
         demons[weak] = 1
    else:
         demons[weak] +=1
k = int(input())
for i in range(k):
    name, power, cnt = input().split()
    if power in demons.keys():
        demons[power] -= int(cnt)
for i in demons.values():
    if i > 0:
        sum+=i
print('Demons left:',sum,sep =" ")