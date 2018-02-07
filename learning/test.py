import numpy as np
a = np.array([1, 2, 3])   # Create a rank 1 array
print(a.size)            # Prints "<class 'numpy.ndarray'>"
b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)
b = b.reshape(3,2)
print(b)