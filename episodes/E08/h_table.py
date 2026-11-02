# The H gate as a table
import numpy as np
s = 1 / np.sqrt(2)
H = np.array([[s, s],
              [s, -s]])
plus = H @ np.array([1, 0])
minus = H @ np.array([0, 1])
print(np.round(plus, 4), np.round(minus, 4))
print(np.round(H @ plus, 4), np.round(H @ minus, 4))
