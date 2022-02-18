import random
name = input('Hello! What is your name?\n')
m = random.randint(0, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20. Take a guess.')
def guess():
    c = 0
    while True:
        n = int(input())
        if n < m:
            print('Your guess is too low.')
            print('Take a guess.')
            c += 1
        elif n > m:
            print('Your guess is too high.')
            print('Take a guess.')
            c += 1
        elif n == m:
            c += 1
            print('Good job,', name , '! You guessed my number in', c, 'guesses!')
            break
        
guess()
           