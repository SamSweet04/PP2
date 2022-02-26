def gen(n):
    for i in range(n,-1,-1):
        yield i 
for i in gen(int(input())):
    print(i)