# E05: Probability and Statistics for Qubits

Video: https://youtu.be/ldnbODlqFXc

## E04 solution
1. `try_count31.py`: 0 to 31 in binary with `format(n, '05b')`. 31 is `11111`, so you need 5 places.
2. `try_patterns.py`: 1 bit makes 2 patterns, 2 bits 4, 3 bits 8, 4 bits 16, 5 bits 32. `2 ** 5` is `32`.
3. `try_nand.py`: `NAND(a, b)` is NOT of AND, written as `1 - a * b`. It gives 1, 1, 1, 0.

## This episode
Run with Python 3.13.5, Qiskit 2.6.1 and Qiskit Aer 0.18.2 (`versions.txt`). Each program has its real output next to it (`.out`):
```
python episodes/E05/outcomes.py      # probabilities in a dict: coin and die add up to 1, even rolls = 0.5
python episodes/E05/frequencies.py   # flip a coin 10 to 10000 times (seed 2026): frequency of 0 gets close to 0.5
python episodes/E05/qubit_probs.py   # exact probabilities after an H gate, with Statevector
python episodes/E05/qubit_shots.py   # measure the same qubit 10 to 10000 times with AerSimulator
python episodes/E05/never_exact.py   # 1000 shots with 5 seeds, and the exact chance of exactly 500 zeros (0.0252)
```

## Your turn (solution in E06)
1. Add `50000` to the shot list in `qubit_shots.py`. Is the frequency closer to 0.5?
2. Roll a die 6000 times with `random.randint(1, 6)` and count each face. About how many of each do you expect?
3. From the same rolls, compute the frequency of even numbers and compare it with the probability 0.5.
