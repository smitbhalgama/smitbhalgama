##f = open("smit.txt","r")
##d= f.readline()
##print(d)
#factorial
def smit(n):
	if(n==1):
		return n
	else:
		return n*smit(n-1)
			
d=smit(5)  		
print("factorial of number",d)