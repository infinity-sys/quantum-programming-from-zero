# Our length-1 arrow [0.6, 0.8] as a qubit
from qiskit.quantum_info import Statevector

sv = Statevector([0.6, 0.8])
print(sv.is_valid())
print(round(0.6 ** 2, 4), round(0.8 ** 2, 4))
for outcome, p in sv.probabilities_dict().items():
    print(outcome, round(float(p), 4))
print(Statevector([3, 4]).is_valid())
