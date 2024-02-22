def smit(x,y):
  if(y==0):
 	 return y
  else:
	 return smit(y,x%y)	

d=smit(4,8)	
print(d)