n = input()
def unique():
    l = []
    for i in n:
        if i not in l:
            l.append(i)
    print(l, end='')

unique()