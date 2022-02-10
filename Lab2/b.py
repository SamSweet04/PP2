n = int(input())
d = list(map(int,input().split()))
d.sort()
print(d[-1]*d[-2])