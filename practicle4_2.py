h = int(input("enter hours"))
w = int(input("enter wages"))
if(h<=40):
	total = h*w
elif(h>40):
	total = 40*w+(h-40)*w*1.5
print("total wages",total)
