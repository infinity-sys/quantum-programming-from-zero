# The exact probabilities of a qubit after an H gate
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1)
qc.h(0)
probs = Statevector(qc).probabilities_dict()
for outcome, p in probs.items():
    print(outcome, float(p), round(float(p), 3))
print(round(float(sum(probs.values())), 3))
