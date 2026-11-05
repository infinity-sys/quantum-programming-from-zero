# Probability = |⟨outcome|psi⟩| squared
import numpy as np
psi = np.array([0.6, 0.8j])
zero = np.array([1, 0])
one = np.array([0, 1])
a0 = np.vdot(zero, psi)
a1 = np.vdot(one, psi)
print('⟨0|psi⟩ =', a0, ' P(0) =', round(abs(a0) ** 2, 4))
print('⟨1|psi⟩ =', a1, ' P(1) =', round(abs(a1) ** 2, 4))
