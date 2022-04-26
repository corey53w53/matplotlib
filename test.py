import matplotlib.pyplot as plt

x_values=[]
y_values=[]
for num in range(1,50):
    x_values.append(num)
    y_values.append(num**2)

plt.plot(x_values,y_values)
plt.show()