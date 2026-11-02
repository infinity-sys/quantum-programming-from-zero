# Shrink an arrow to length 1
import numpy as np
v = np.array([3, 4])
u = v / np.linalg.norm(v)
print(u)
print(np.linalg.norm(u))
