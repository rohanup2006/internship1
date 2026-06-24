import numpy as np
# Coefficient matrix
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
# Right-hand side vector
b = np.array([9, -6, 17])
# Solve for x, y, z
solution = np.linalg.solve(A, b)
print("Solution (x, y, z):", solution)