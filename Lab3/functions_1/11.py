s = str(input())
def palindrome():
    t = s[::-1]
    if s == t:
        print('True')
    else:
        print('False')

palindrome()
