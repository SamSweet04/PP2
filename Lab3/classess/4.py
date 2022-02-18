from math import sqrt
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(f'Coordinates of the point are {self.a} and {self.b}')

    def change(self, a1, b1):
        self.a = a1
        self.b = b1
        print(f'New coordinates are {a1} and {b1}')

    def dist(self, a1, b1):
        self.a1 = a1
        self.b1 = b1
        print(sqrt((self.a - a1) ** 2 + (self.b - b1) ** 2))

P = Point(int(input()), int(input()))
P.show()
P.change(int(input()), int(input()))
P.dist(int(input()), int(input()))
