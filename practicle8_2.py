def smit(m):
	for i in m:
		if (m.count(i)>1):
			m.remove(i)

	return m		
	
n = [1,1,'smit','smit',12,'keyur']
c = smit(n)
print(c)  