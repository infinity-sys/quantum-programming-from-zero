# Kets are columns: |0⟩, |1⟩ and |+⟩
import numpy as np
from qiskit.quantum_info import Statevector

for label in ['0', '1', '+']:
    ket = Statevector.from_label(label)
    print(label, np.round(ket.data.real, 4))
