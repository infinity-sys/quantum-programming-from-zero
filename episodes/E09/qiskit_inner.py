# Qiskit agrees: inner, probabilities, and real shots
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

psi = Statevector([0.6, 0.8j])
zero = Statevector.from_label('0')
print(np.round(zero.inner(psi), 4))
print(np.round(psi.probabilities(), 4))

qc = QuantumCircuit(1)
qc.initialize(psi, 0)
qc.measure_all()
sim = AerSimulator(seed_simulator=9)
print(sim.run(qc, shots=1000).result().get_counts())
