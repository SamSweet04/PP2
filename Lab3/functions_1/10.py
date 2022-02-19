n = input().split()
def unique():
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    print(*l, sep=' ')
unique()
