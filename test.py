import matplotlib.pyplot as plt
import numpy as np

a=np.sort([1,3,2,4,6,5])

print(type(a))
x_values=[]
y_values=[]
for num in range(1,50):
    x_values.append(num)
    y_values.append(num**2)

plt.plot(x_values,y_values)
# plt.show()