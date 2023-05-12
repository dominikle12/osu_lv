import numpy as np
import matplotlib . pyplot as plt

plt.axes()
line = plt.Line2D((1, 3), (1, 1), lw=1.5, marker=".")
line1 = plt.Line2D((3, 3), (1, 2), lw=1.5, marker=".")
line2 = plt.Line2D((2, 3), (2, 2), lw=1.5, marker=".")
line3 = plt.Line2D((1, 2), (1, 2), lw=1.5, marker=".")
plt.gca().add_line(line)
plt.gca().add_line(line1)
plt.gca().add_line(line2)
plt.gca().add_line(line3)
plt.axis([0, 4 , 0, 4])
plt.show()



