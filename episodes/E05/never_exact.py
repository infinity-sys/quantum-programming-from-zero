# Five runs of 1000 shots: the counts are never the same
from math import comb
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
for seed in [1, 2, 3, 4, 5]:
    sim = AerSimulator(seed_simulator=seed)
    counts = sim.run(qc, shots=1000).result().get_counts()
    print('seed', seed, counts)
# the chance of exactly 500 zeros in 1000 shots
print(round(comb(1000, 500) / 2 ** 1000, 4))
