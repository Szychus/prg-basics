###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a,b,c):
      s = (a + b + c) / 2
      heron = math.sqrt(s * (s - a) * (s - b) * (s - c))
      return heron

print('Input triangle sides')
a = float(input('Side a: '))
b = float(input('Side b: '))
c = float(input('Side c: '))



print(f'The area of ​​a triangle with sides:  {a}  {b}  {c} is {triangle_area(a, b, c)}')