f = int(input())
a = [['.' for i in range(f)] for j in range(f)]
for i in range(f):
    for j in range(f):
        if(f % 2 == 0):
            if(i >= j):
                a[i][j] = '#'
        else:
            if(i + j >= f - 1):
                a[i][j] = '#'
for i in range(f):
    for j in range(f):
        print(a[i][j], end="")        
    print()