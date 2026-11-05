# Normalise: divide by the length so that ⟨psi|psi⟩ = 1
import numpy as np
v = np.array([3, 4])
print('⟨v|v⟩ =', np.vdot(v, v))
length = np.sqrt(np.vdot(v, v))
psi = v / length
print('length =', length)
print('psi =', psi)
print('⟨psi|psi⟩ =', round(np.vdot(psi, psi), 4))
