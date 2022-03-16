s = input()
uppercase,lowercase = 0,0
for i in s:
    if 65<=ord(i)<=90:
        uppercase+=1
    elif 97<=ord(i)<=122:
        lowercase+=1
print(f'Uppercase letters are: {uppercase}')
print(f'Lowercase letters are: {lowercase}')


