def smit(n):
	if(n<=1):
		return n
	else:
		return smit(n-1)+smit(n-2)
d=int(input("enter number"))
for i in range(d):
	print("fibo of ",smit(i))			