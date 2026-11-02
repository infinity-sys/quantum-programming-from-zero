# E06: Vectors Without Fear

Video: VIDEO_LINK_PLACEHOLDER

## E05 solution
1. `try_50000.py`: the same H-gate qubit with seed 2026, now with `50000` shots. The frequency of 0 is `0.50202`, about 0.002 from 0.5 (10000 shots were about 0.003 away).
2. `try_die.py`: 6000 rolls with `random.randint(1, 6)` (seed 2026). Each face comes up between 964 and 1067 times; about 1000 was expected.
3. Same file: the even faces add up to 2949 rolls, a frequency of `0.4915`, close to the probability 0.5 but not equal.

## This episode
Run with Python 3.13.5, Qiskit 2.6.1 and Qiskit Aer 0.18.2 (`versions.txt`). Each program has its real output next to it (`.out`):
```
python episodes/E06/arrow_length.py      # a vector as a list, and its length with Pythagoras: [3, 4] has length 5.0
python episodes/E06/add_scale.py         # add two vectors component by component, and multiply by a scalar
python episodes/E06/numpy_vectors.py     # the same with NumPy arrays, and np.linalg.norm
python episodes/E06/unit_vector.py       # normalise [3, 4] into the unit vector [0.6, 0.8]
python episodes/E06/qubit_column.py      # qubit states as columns of two numbers, each with length 1
python episodes/E06/squares_to_probs.py  # square the amplitudes to get probabilities; [3, 4] is not a valid state
```

## Your turn (solution in E07)
1. What is the length of the vector `[5, 12]`? Work it out by hand, then check with `np.linalg.norm`.
2. Normalise `[1, 1]`: divide it by its length and print it. Have you seen those numbers before?
3. Give `[0.8, 0.6]` to Qiskit's `Statevector`. Is it valid? What are its probabilities? What does `is_valid()` say for `[1, 1]`?
