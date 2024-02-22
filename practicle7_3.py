# create dictionary

d = {1:"smit",2:12,3:2.5}

# print dictionary

print(d)

# add dictionary

d['a']="cusp"
print(d)

#remove dictionary
a=d.pop(2)
print(a)
print(d)

a=d.popitem()
print(a)
print(d)


#check key exits
n = 30
if(n in d):
	print("key found")
else:
	print("key not found")	

# itrate dictionary
for i in d:
		print(d[i])

# concatenate dictionary
d.update({'b':22,45:3})
print(d)		

