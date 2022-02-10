#print(list(map(len,p.split())))
p = input()
def words(s):
    d = p.split(' ')
    for word in d:
        if len(word)>=3:
            print(word, end=" ")
words(p)