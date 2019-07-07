import numpy as np

# batting average experiment
batting_ave = np.array([0.336, 0.281, 0.238, 0.245])
print("batting averages: " + str(batting_ave))
print(batting_ave.mean())

a = np.ones((2, 3))+1
b = np.ones((3, 2))

# matrix multiplication is done with .dot() method
print(a.dot(b))

stats = np.array([[4, 1], [4, 0], [5, 3], [4, 0]])

# population example
data = np.loadtxt('populations.txt')
print(data)




