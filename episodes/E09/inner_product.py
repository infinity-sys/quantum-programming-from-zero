# The inner product ⟨a|b⟩: bra row times ket column
import numpy as np
s = 1 / np.sqrt(2)
zero = np.array([1, 0])
one = np.array([0, 1])
plus = np.array([s, s])
print('⟨0|0⟩ =', np.vdot(zero, zero))
print('⟨0|1⟩ =', np.vdot(zero, one))
print('⟨0|+⟩ =', round(np.vdot(zero, plus), 4))
print('⟨+|+⟩ =', round(np.vdot(plus, plus), 4))
