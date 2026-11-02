# E06 task 3: is it a qubit?
from qiskit.quantum_info import Statevector
sv = Statevector([0.8, 0.6])
print(sv.is_valid())
for outcome, p in sv.probabilities_dict().items():
    print(outcome, round(float(p), 4))
print(Statevector([1, 1]).is_valid())
