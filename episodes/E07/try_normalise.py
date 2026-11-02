# E06 task 2: normalise [1, 1]
import numpy as np
v = np.array([1, 1])
u = v / np.linalg.norm(v)
print(np.round(u, 4))
