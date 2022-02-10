n = int(input())
students = {}
students1 = {}
for i in range(n):
    a,b = map(str, input().split())
    if students.get(a,0) == 0:
        students[a] = int(b)
    else:
        students[a] += int(b)
max_key= max(students, key=students.get)
all_values = students.values()
max_value = max(all_values)
for k,v in students.items():
    students[k] = int(max_value - v)
for k,v in sorted(students.items()):
    if v == 0:
        k = k +' '+ 'is lucky!'
    else:
        k = k +' '+ 'has to receive' + ' '+ str(v) + ' '+'tenge'
    print(k)






