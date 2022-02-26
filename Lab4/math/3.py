import math
sides = int(input('Input number of sides:'))
length_of_sides = int(input('Input the length of a side:'))
print(f'The area of the polygon is: {int(sides*(length_of_sides**2)/(4*math.tan(math.pi/sides)))}')