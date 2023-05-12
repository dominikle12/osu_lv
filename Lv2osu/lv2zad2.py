import numpy as np
import matplotlib.pyplot as plt

arr = np.loadtxt(open("data.csv"),delimiter=",", skiprows=1)
print("Mjerenja su izvrsena na "+str(arr.shape[0])+" osoba")   

#a)
height = arr[:,1]
weight = arr[:,2]

h2=height[::50]
w2=weight[::50]

#b)
plt.scatter(height, weight)
plt.axis([100, 230 , 0, 230])
plt.show()  

#c)
plt.scatter(h2, w2)
plt.axis([100, 230 , 0, 230])
plt.show()  

#d)
print("Max visina: "+ str(max(height)))
print("Min visina: "+ str(min(height)))
print("Srednja visina: "+ str(np.mean(height)))


rows=np.where(np.arr[:,0]==1)