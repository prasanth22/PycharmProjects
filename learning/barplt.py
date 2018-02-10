from matplotlib import pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2],label = "Ex1")
plt.bar([2,4,6,8,10],[8,6,2,5,6],label = "Ex2",color='g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar heigth')
plt.title('info')
plt.show()