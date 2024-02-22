def s(n):
	if (n == 1):
		return n
	else:
		return n * s(n-1)
a=int(input("enter number"))
x=s(a)
print("fectorial",x)			