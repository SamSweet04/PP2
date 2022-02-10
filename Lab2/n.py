num,summa = [],[]
while True:
    n = int(input())
    if n == 0:
        break
    else:
        num.append(n)
for i in range(len(num)//2):
    summa.append(num[i] + num[len(num)-i-1])
if len(num) % 2 == 0:
     pass
else:
    summa.append(num[len(num)//2])
print(*summa)
