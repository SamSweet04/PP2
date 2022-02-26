import math
def squares(a,b):
    start = a
    end = b
    for i in range(start,end+1):
        yield i*i
for i in squares(int(input()),int(input())):
    print(f'{i}<--->{int(math.sqrt(i))}')
