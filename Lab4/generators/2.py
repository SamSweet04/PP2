list = []
def even_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
for i in even_gen(int(input())):
    list.append(str(i))
print(",".join(list))

