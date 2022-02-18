from itertools import permutations
s = input()
def perm(): 
    l = permutations(s) 
    for i in list(l):       
       print(i) 
perm()
