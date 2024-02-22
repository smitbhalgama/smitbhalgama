# ctreate two sets with data
s = {1,2.4,"smit",23}
s1 = {"cusp",12.3,"bhalgama",23,"smit"}
# print set item
for i in s:
	print(i)
for x in s1:
	print(x)	
# add item in set
s.add(21)
print(s)

s1.add("keyur")
print(s1)
# delete item in set
s.remove(1)
print(s)

s1.discard("cusp")
print(s1)

b = s1.pop()
print(s1)
print(b)

# perform union oprator
b1 = s.union(s1)
print(b1)

# perform intersaction oprator
b1 = s.intersection(s1)
print(b1)

# perform  oprator
b1 = s.difference(s1)
print(b1)

# perform symmetric difference oprator
b1 = s.symmetric_difference(s1)
print(b1)