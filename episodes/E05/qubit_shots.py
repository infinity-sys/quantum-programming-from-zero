# Measure the same qubit with more and more shots
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
sim = AerSimulator(seed_simulator=2026)
for shots in [10, 100, 1000, 10000]:
    counts = sim.run(qc, shots=shots).result().get_counts()
    print(shots, counts, counts.get('0', 0) / shots)
