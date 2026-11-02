# Z and S only change the phase of the 1 amplitude
import numpy as np
Z = np.array([[1, 0],
              [0, -1]])
S = np.array([[1, 0],
              [0, 1j]])
s = 1 / np.sqrt(2)
plus = np.array([s, s])
print(np.round(Z @ plus, 4))
print(np.round(S @ plus, 4))
print(np.round(np.abs(S @ plus) ** 2, 4))
