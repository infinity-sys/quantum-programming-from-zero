# A qubit with a complex amplitude
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.h(0)
qc.s(0)
sv = Statevector(qc)
print(np.round(sv.data, 4))
print(np.round(np.abs(sv.data) ** 2, 4))
