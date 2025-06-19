import numpy as np

# Define two sample matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Element-wise addition
add_result = np.add(A, B)

# Element-wise multiplication
multiply_result = np.multiply(A, B)

# Display results
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Element-wise Addition:\n", add_result)
print("Element-wise Multiplication:\n", multiply_result)
