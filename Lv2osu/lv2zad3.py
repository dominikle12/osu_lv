import numpy as np
import matplotlib.pyplot as plt

img = plt.imread ("road.jpg")
img = img [:,:,0].copy()


plt.figure()
plt.imshow(img, cmap="gray", alpha=0.5)
plt.show()

width=len(img.T)
plt.figure()
plt.imshow(img[:, int(width/4):int(width/4+width/4)], cmap="gray")
plt.show()

plt.figure()
plt.imshow(np.rot90(img, 3), cmap="gray")
plt.show()

plt.figure()
plt.imshow(np.fliplr(img), cmap="gray")
plt.show()