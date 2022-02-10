f = int(input())
arr = [[0 for i in range(f)] for i in range(f)]
for i in range(f):
    for j in range(f):
        if(i == j):
            arr[i][j]= i * j
        if(i * j == 0):
            arr[i][j] = i
            arr[j][i] = i
for i in range(f):
    for j in range(f):
        print(arr[i][j],end = " ")
    print()