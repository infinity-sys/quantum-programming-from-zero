# Episode 8 task 2: X, then H, on the qubit 0
import numpy as np
s = 1 / np.sqrt(2)
X = np.array([[0, 1],
              [1, 0]])
H = np.array([[s, s],
              [s, -s]])
zero = np.array([1, 0])
print(X @ zero)
print(np.round(H @ (X @ zero), 4))
