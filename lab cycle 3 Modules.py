#....graphics
#....rectangle.py
def area_rectangle(l,b):
	return l*b
def perimeter_rectangle(l,b):
	return 2*(l+b)

#....circle.py
from math import pi
def area_circle(r):
	return pi*r*r
def perimeter_circle(r):
	return 2*pi*r

#....__init__.py
from .circle import *
from .rectangle import * 

#....graphics_3d
#....sphere.py
from math import pi
def area_sphere(r):
	return 4*pi*r*r
def perimeter_sphere(r):
   return (4/3)*pi*r*r*r
  
#.....cuboid.py
def area_cuboid(l,b,h):
	return 2*(l*b + b*h + l*h)
def perimeter_cuboid(l,b,h):
	return 4*(l+b+h)

#....__init__.py
from .cuboid import *
from .sphere import * 

#....package.py
from graphics import *
from graphics.graphics_3d import *

r=int(input("enter radius"))
print("area of circle is",area_circle(r))
print("perimeter of circle is",perimeter_circle(r))

l=int(input("enter length"))
b=int(input("enter breadth"))	
print("area of rectangle is",area_rectangle(l,b))
print("perimeter of rectangle is",perimeter_rectangle(l,b))

l=int(input("enter lenth"))
b=int(input("enter breadth"))
h=int(input("enter heigth"))
print("area of cuboid is",area_cuboid(l,b,h))
print("area of cuboid is",perimeter_cuboid(l,b,h))

r=int(input("enter the radius"))
print("area of sphere is",area_sphere(r))
print("perimeter of sphere is",perimeter_sphere(r))










