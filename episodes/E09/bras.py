# A bra is the ket turned into a row, with i flipped to -i
import numpy as np
ket = np.array([0.6, 0.8j])
bra = ket.conj()
print('ket:', ket)
print('bra:', bra)
