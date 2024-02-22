import math
h=int(input("enter hight of the wall:"))
a=int(input("enter angle in degrees:"))
a_radians = math.radians(a)
l=h/math.sin(a_radians)
print(l)