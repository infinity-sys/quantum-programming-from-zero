# The X gate as a table: it swaps the amplitudes
import numpy as np
X = np.array([[0, 1],
              [1, 0]])
print(X @ np.array([1, 0]))
print(X @ np.array([0.6, 0.8]))
