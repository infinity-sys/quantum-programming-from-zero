# Ask Qiskit for the table, and check it
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector

qc = QuantumCircuit(1)
qc.h(0)
print(np.round(Operator(qc).data.real, 4))
print(np.round(Statevector.from_label('0').evolve(qc).data.real, 4))
