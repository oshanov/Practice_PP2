#First: Write a Python program to convert degree to radian.
import math

x = float(input())
y = math.radians(x)
print(y)

#Second: Write a Python program to calculate the area of a trapezoid.
height, base1,base2 = map(int, input().split())
area = (base1 + base2) / 2 * height
print(area)

#Third: Write a Python program to calculate the area of regular polygon.

n, a = map(int, input().split())
area = int((n * a**2)/ (4 * math.tan(math.pi/n)))
print(area)

#Fourth: Write a Python program to calculate the area of a parallelogram.

a,h = map(int,input().split())
area = a * h
print(float(area))