n = input().split()
def histogram():
    for i in n:
        i = int(i)
        for j in range(i):
            print('*', end='')
        print()
        
histogram()