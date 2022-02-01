import numpy as np


a = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])

print("Dimension:",a.ndim)
print("Forma de la matriz:", a.shape)
print("Cantidad de elementos en la matriz:", a.size)
print("Matriz a:", a)
a_transposed = a.T
print(a_transposed)
a=np.array([-1,1])
b=np.array([1,1])
x = np.dot(a,b) 
print(x)