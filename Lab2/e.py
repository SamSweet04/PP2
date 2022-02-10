s = str(input())
if " " not in s:
    x = int(input())
    n = int(s)
else:
    s = s.split()
    n = int(s[0])
    x = int(s[1])
arr = []
for i in range(int(n)):
    d = int(x) + 2*int(i)
    arr.append(d)
k = arr[0]
for i in range(len(arr)-1):
    k = k ^ arr[i+1]
print(k)