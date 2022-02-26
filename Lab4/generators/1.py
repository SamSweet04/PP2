def generator(n):
    for i in range(n):
        yield i**2
for i in generator(int(input())):
    print(i)