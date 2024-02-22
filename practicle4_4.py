m=int(input("enter maths mark::"))
s=int(input("enter science mark::"))
p=int(input("enter physics mark::"))
per=(m+s+p)/3;
print("per is",per)
if(per>=90):
	print("grade A")
elif(per>=80 and per<=89):
	print("grade B")
elif(per>=70 and per<=79):
	print("grade c")
elif(per>=60 and per<=69):
	print("grade D")
elif(per>=50 and per<=59):
	print("grade E")
else:
	print("grade f")
