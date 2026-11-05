# Episode 8 task 3: ask Qiskit for the X table
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

qc = QuantumCircuit(1)
qc.x(0)
print(Operator(qc).data.real)
