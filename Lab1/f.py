a =int(input())
for i in range(0,a):
    d = int(input())
    if d<=10:
        print('Go to work!') 
    elif 10 < d <= 25:
        print('You are weak')
    elif 25 < d <= 45:
        print('Okay, fine')
    elif d>45:
        print('Burn! Burn! Burn Young!')
    else:
        print('')