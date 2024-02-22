from matplotlib import pyplot as plt
x = [1,3,5,7,9]
y = [10,11,10,11,16]
x1 = [2,4,6,8,10]
y1 = [7,9,5,7,9]

plt.bar(x,y,color='azure',background='beige')
plt.bar(x1,y1,color='yellow')
plt.xlabel("overs")
plt.ylabel("runs")
plt.show()
