import matplotlib.pyplot as plt
import numpy as np
import random

l1=[a for a in range(100000)]
l2=l1.copy()
random.shuffle(l2)
print(l2)

x_values=[]
y_values=[]
for c in range(len(l1)):
    x_values.append(l1[c])
    y_values.append(l2[c])
plt.plot(x_values,y_values)
plt.show()