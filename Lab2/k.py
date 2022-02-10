s  = input()
t = ""
l = set()
for i in range(len(s)):
    if((s[i]>='A' and s[i]<='Z') or (s[i]>='a' and s[i]<='z') or s[i] == ' '):
        t+=s[i]
for word in t.split():
     l.add(word)
print(len(l))
print(*sorted(l),sep='\n')

    

    