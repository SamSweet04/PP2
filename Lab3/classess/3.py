class Shape:
    def __init__(self):
        pass

    def area1(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area2(self):
        return self.length*self.height

A = Rectangle(int(input()), int(input()))
print(A.area2())