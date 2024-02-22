d = {"gujrat":"gandhinagar","up":"lucknow","mp":"bhopal","punjab":"chandigadh"}
st = input("enter state:")
while (True):
	cap = input("enter capital of"+st+":")
	if (d[st]==cap):
		print("correct...")
		break
	else:
		print("incorrect...")	
