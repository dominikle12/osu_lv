import numpy as np
import matplotlib . pyplot as plt

white=np.zeros([50,50,3],dtype=np.uint8)
black=np.ones([50,50,3],dtype=np.uint8)
white.fill(255)
black.fill(0)

row1=np.hstack((black,white))
row2=np.hstack((white,black))
img=np.vstack((row1,row2))

plt.figure()
plt.imshow(img)
plt.show()