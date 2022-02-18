import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x1, y1):
        self.x = x1
        self.y = y1
        print(self.x, self.y)

    def dist(self, x, y, x1, y1):
        return math.sqrt((x1-x)*(x1-x) + (y1-y)*(y1-y))

F1 = Point(int(input()), int(input()))
F2 = Point(int(input()), int(input()))
F3 = Point(F1, F2)
print(F1.show())
print(F2.move())
print(F3.dist())
