import random
def myshuffle(n):
	random.shuffle(n)
	return n
n = [1,'smit',12,'keyur']
c = myshuffle(n)
print(c)  