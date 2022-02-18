n = input().split()
def has_33():
    c = False
    for i in range(len(n) - 1):
        if n[i] == '3' and n[i+1] == '3':
            c = True
        else: continue

    if c: print('True')
    else: print('False')  
has_33()