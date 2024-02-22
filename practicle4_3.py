h = int(input("enter height"))
w = int(input("enter weight"))
h = h/100
bmi = w/h**2
print("bmi is",bmi)
if(bmi<19):
	print("underwighit")
elif(bmi>=19 and bmi<=25):	
	print("health")
elif(bmi>25):
    print("overwighit")	