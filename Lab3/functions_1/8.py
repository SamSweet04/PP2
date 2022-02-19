n = input().split(',')
def spy_game():
    s = ''
    for i  in n:
        if i == '0' or i == '7':
            s += i

    if s == '007': print('True')
    else: print('False')
    
spy_game()
