from functions import *
print(*list(filter(lambda x: (is_prime(x)), list(map(int, input().split())))))

class Primes:
    def __init__(self, x):
        self.x = x

    def is_prime(self):
        if self.x == 1: return False
        for i in range(2, self.x):
            if self.x % i == 0:
                return False
        return True
a, res = list(map(int, input().split())), []
for i in a:
    n = Primes(i)
    if n.is_prime():
        res.append(i)
print(*res)