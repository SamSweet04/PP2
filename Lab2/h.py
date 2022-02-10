def dis(x,y,x2,y2):
    return (x-x2)*(x-x2)+(y-y2)*(y-y2)
dict = {}
x,y = map(int,input().split())
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    d = dis(x,y,a,b)
    if d not in dict:
        dict[d] = [a,b]
    else:
        dict[d].append(a)
        dict[d].append(b)
for k in sorted(dict.keys()):
      v = dict[k]
      if len(v)>2:
          for i in range(0,len(v),2):
              print(v[i],v[i+1])
      else:
          print(*dict[k])

