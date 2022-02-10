a= int(input())
for i in range(0,a):
    d = input()
    if d[-10:] == '@gmail.com':
        print(d.replace('@gmail.com', ''))
    else:
        continue