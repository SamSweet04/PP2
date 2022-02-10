d =input()
res = 0
for p in d:
    res+=(ord(p))
if res > 300:
    print("It is tasty!")
else:
    print("Oh, no!")