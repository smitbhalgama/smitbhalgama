import cmath
a = int(input("enter value of a"))
b = int(input("enter value of b"))
c = int(input("enter value of c"))
d=(b**2)-(4*a*c)
r1=((-b)+cmath.sqrt(d))/2*a
r2=((-b)-cmath.sqrt(d))/2*a
print("root 1::",r1)
print("root 2::",r2)