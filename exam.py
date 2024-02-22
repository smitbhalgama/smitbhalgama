# l=[10,"smit","rudra","shivam",15.7]
# print(l)
# l.insert(1,"abc")
# print(l)
# l.append(30)
# print(l)
# l.extend([1,2,3])
# print(l)

# l.remove(30)
# print(l)
# x=l.pop(1)
# print(x)

# c=0
# for i in l:
# 	c=c+1
# print(c)

# print(l[1])

# l1=[12,30,50,25,60]
# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

# 2nd exercise of list
# l=[]
# a=int(input("Enter number of elements to enter:"))
# for i in range(0,a):
# 	l.append(input("Enter values:"))
# print(l)
# e=0
# for b in l:
# 	if(b>0):
# 		e=e+1
# print("Positive:",e)

# e=0
# for b in l:
# 	if(b<0):
# 		e=e+1
# print("negative:",e)

# e=0
# for b in l:
# 	if(b==0):
# 		e=e+1
# print("Zero:",e)

# e=0
# for b in l:
# 	if(b%2==0):
# 		e=e+1
# print("Even:",e)

# e=0
# for b in l:
# 	if(b%2!=0):
# 		e=e+1
# print("Odd:",e)
# s=0
# i=0
# for b in l:
# 	s=s+b
# 	i=i+1
# avg=s/i
# print("Average:",avg)


# l="12203AB3"
# for i in l:
# 	x=l.count(i)
# 	print(i,"-->",x)

# l=[1,2,5,1,2]
# s=set(l)
# l1=list(s)
# print(l1)

# tuple
# t=(10,15.7,"abc")
# print(t)

# l1=list(t)
# print(l1)

# l1.remove(15.7)
# print(l1)

# t=tuple(l1)
# print(t)

# set
# s1={10,15.7,"abc","smit"}
# s2={20,30.7,"def","rudra"}
# print(s1)
# print(s2)

# s1.add("shivam")
# print(s1)

# s1.remove("abc")
# print(s1)

# dictionary
d={1:"smit",2:"rudra",3:"shivam",4:"10"}
print(d)

d.update({5:"15.7"})
print(d)

d.pop(2)
print(d)

d1=int(input("Enter keys:"))
f=0
a=d.keys()
print(a)
for i in a:
	if d1==i:
		f=1
		break
if f==1:
	print(True)
else:
	print(False)