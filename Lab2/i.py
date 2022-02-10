n = int(input())
putting, taking = [], []
for i in range(n):
    shelf = input().split()
    if len(shelf) == 2:
         disks = (shelf[1])
         putting.append(disks)
    else:
        taking.append(putting[0])
        putting.pop(0)
print(*taking)

    