def bin(s):
    if len(s) == 1:
         return int(s)
    else:
         return bin(s[-1]) + 2*bin(s[:-1])
s = str(input())
print(bin(s))