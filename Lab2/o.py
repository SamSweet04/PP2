numbers = {
    'ONE' : '1',
    'TWO' : '2', 
    'THR' : '3', 
    'FOU' : '4', 
    'FIV' : '5', 
    'SIX' : '6', 
    'SEV' : '7', 
    'EIG' : '8', 
    'NIN' : '9', 
    'ZER' : '0' }
numb = {}
s = input().split('+')
a,b = '' , ''
for i in range(0,len(s[0]),3):
    a += numbers[s[0][i:i+3]]
for i in range(0,len(s[1]),3):
    b += numbers[s[1][i:i+3]]
for k,v in numbers.items():
    numb[numbers[k]] = k
for i in str(int(a)+int(b)):
    print(numb[i],end ='')

