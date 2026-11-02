# A qubit is a column of two numbers
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

zero = Statevector.from_label('0')
one = Statevector.from_label('1')
qc = QuantumCircuit(1)
qc.h(0)
plus = Statevector(qc)
for name, sv in [('zero', zero), ('one', one), ('after H', plus)]:
    col = np.round(sv.data.real, 4)
    print(name, col, round(float(np.linalg.norm(sv.data)), 4))
