def prime(n):
	f = 0
	for i in range(2,n):
		if(n%i==0):
			f=1
			break
	if(f==0):
	   print("prime")
	else:
		print("not prime")
n = int(input("enter value"))
prime(n)			   		