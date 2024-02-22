
c = 5
for i in range(1,6):
	print(' ' * c,end = ' ')
	c = c-1

	for j in range(1,i+1):
		print("*",end = ' ')

	print(end = '\n')	
