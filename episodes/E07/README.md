# E07: Complex Numbers, From Zero

Video: VIDEO_LINK_PLACEHOLDER

## E06 solution
1. `try_length.py`: the length of `[5, 12]` is the square root of 25 + 144 = 169, so 13. `np.linalg.norm` prints `13.0`.
2. `try_normalise.py`: `[1, 1]` has length the square root of 2 (about 1.4142). Divided by it, it becomes `[0.7071 0.7071]`, the qubit after an H gate.
3. `try_qubit.py`: `Statevector([0.8, 0.6])` is valid (`True`), with probabilities 0.64 for 0 and 0.36 for 1. `[1, 1]` is not valid (`False`): its squares add up to 2.

## This episode
Run with Python 3.13.5, Qiskit 2.6.1 and Qiskit Aer 0.18.2 (`versions.txt`). Each program has its real output next to it (`.out`):
```
python episodes/E07/complex_basics.py     # 1j * 1j is -1; real and imaginary parts; abs(3+4j) is 5.0
python episodes/E07/complex_arith.py      # add, multiply and conjugate complex numbers
python episodes/E07/times_i.py            # multiplying by 1j four times turns a full circle
python episodes/E07/magnitude_phase.py    # magnitude with abs, phase with cmath.phase in degrees
python episodes/E07/complex_amplitude.py  # H then S: a complex amplitude, probabilities still 0.5 and 0.5
python episodes/E07/phase_matters.py      # same probabilities, different phase, different result after a second H
```

## Your turn (solution in E08)
1. What is `abs(5 + 12j)`? Guess first, then run it.
2. Multiply `1 + 1j` by `1j`, by hand and in Python. What is the phase before and after? By how many degrees did it turn?
3. Give `Statevector` the amplitudes `[0.6, 0.8j]`. Is it valid? What are its probabilities?
