# E08: Matrices as Gate Tables

Video: VIDEO_LINK_PLACEHOLDER

## E07 solution
1. `try_abs.py`: `abs(5 + 12j)` is the length of the arrow 5 across and 12 up, the same as the vector `[5, 12]` from E06. It prints `13.0`.
2. `try_turn.py`: by hand, (1 + j) times j is j + j*j = -1 + j. Python prints `(-1+1j)`. The phase goes from 45.0 to 135.0 degrees: a quarter turn of 90 degrees.
3. `try_complex_qubit.py`: `Statevector([0.6, 0.8j])` is valid (`True`). The magnitudes are 0.6 and 0.8, so the probabilities are 0.36 for 0 and 0.64 for 1. The `j` does not change the probability.

## This episode
Run with Python 3.13.5, Qiskit 2.6.1 and Qiskit Aer 0.18.2 (`versions.txt`). Each program has its real output next to it (`.out`):
```
python episodes/E08/table_by_hand.py  # a 2 x 2 table times a column, by hand: [4, 6]
python episodes/E08/numpy_table.py    # the same with NumPy and the @ sign
python episodes/E08/x_table.py        # the X gate as a table swaps the amplitudes
python episodes/E08/h_table.py        # the H gate as a table: two mixes, and H twice gives the start back
python episodes/E08/z_s_tables.py     # Z and S only change the phase of the 1 amplitude
python episodes/E08/qiskit_table.py   # Qiskit's Operator gives the same H table
```

## Your turn (solution in E09)
1. By hand, multiply the table `[[1, 2], [3, 4]]` by the column `[1, 1]`. Then check with the `@` sign.
2. Apply X and then H to the qubit `[1, 0]`, as tables. Which column do you get? Is it one of the two mixes from today?
3. Use `Operator` to print the table of a circuit with an X gate, and compare it with ours.
