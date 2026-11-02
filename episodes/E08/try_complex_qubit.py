# E07 task 3: a complex qubit
from qiskit.quantum_info import Statevector
sv = Statevector([0.6, 0.8j])
print(sv.is_valid())
for outcome, p in sv.probabilities_dict().items():
    print(outcome, round(float(p), 4))
