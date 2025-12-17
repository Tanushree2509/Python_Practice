import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5])
mylabels = ['A', 'B', 'C', 'D', 'E']
plt.pie(x, labels = mylabels, startangle=90)
plt.show()