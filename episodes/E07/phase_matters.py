# Same probabilities, different phase, different results
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def probs(qc):
    d = Statevector(qc).probabilities_dict(decimals=4)
    return {str(k): float(v) for k, v in d.items()}

for name in ['H, H', 'H, S, H', 'H, Z, H']:
    qc = QuantumCircuit(1)
    qc.h(0)
    if 'S' in name:
        qc.s(0)
    if 'Z' in name:
        qc.z(0)
    before = probs(qc)
    qc.h(0)
    print(name, before, probs(qc))
