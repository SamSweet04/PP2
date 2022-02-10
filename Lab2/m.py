l = []
while True:
    d = input()
    if d == '0':
        break
    else:
        l.append(d.split()[2] + ' ' + d.split()[1] + ' ' + d.split()[0])
for i in sorted(l):
    print(i.split()[2] + ' ' + i.split()[1] + ' ' + i.split()[0])