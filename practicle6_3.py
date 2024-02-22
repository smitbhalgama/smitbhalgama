l = []
for i in range(10):
	l.append(int(input("enter value of list")))

print(l)
# print positive number
p = 0	
for i in l:
    if(i>0):

      p = p+1
print("number of positive num:",p)

# print nagative number
n = 0	
for i in l:
    if(i<0):
      n = n+1
print("number of nagative num:",n)

# print zero number
z = 0	
for i in l:
    if(i==0):
      z = z+1
print("number of zero num:",z)

# print even number
z = 0	
for i in l:
    if(i%2==0):
      z = z+1
print("number of even num:",z)


# print odd number
z = 0	
for i in l:
    if(i%2==1):
      z = z+1
print("number of odd num:",z)


# print avg number
z = 0	
for i in l:
    z = i+1/10

print(z)
