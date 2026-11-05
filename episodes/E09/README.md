# E09: Kets, Bras and the Inner Product

Video: https://youtu.be/ADG3xA-PJBU

## E08 solution
1. `try_by_hand.py`: by hand, the first row 1, 2 gives 1·1 + 2·1 = 3 and the second row 3, 4 gives 3·1 + 4·1 = 7. With the `@` sign it prints `[3 7]`.
2. `try_two_gates.py`: X turns `[1, 0]` into `[0, 1]`, then H gives `[0.7071 -0.7071]`: the second mix from E08, the one with the minus sign.
3. `try_operator_x.py`: `Operator` of a circuit with one X gate prints `[[0. 1.] [1. 0.]]`, the same as our X table.

## This episode
Run with Python 3.13.5, Qiskit 2.6.1 and Qiskit Aer 0.18.2 (`versions.txt`). Each program has its real output next to it (`.out`):
```
python episodes/E09/kets.py                 # kets as columns: |0⟩, |1⟩ and |+⟩ from Qiskit labels
python episodes/E09/bras.py                 # a bra is the ket as a row, with every i flipped to -i (conj)
python episodes/E09/inner_product.py        # ⟨a|b⟩ with np.vdot: 1, 0, 0.7071 and 1.0
python episodes/E09/normalise.py            # divide [3, 4] by its length 5: ⟨psi|psi⟩ = 1
python episodes/E09/overlap_probability.py  # the Born rule: P(0) = 0.36, P(1) = 0.64
python episodes/E09/qiskit_inner.py         # Statevector.inner, probabilities, and 1000 real shots on Aer
```

## Your turn (solution in E10)
1. By hand, find the inner product of |+⟩ with |1⟩. Then check it with `np.vdot`.
2. Normalise the column `[1, 1]`. What is its length, and which state from today do you get?
3. For the state `[0.8, 0.6j]`, compute the probability of 1 with the Born rule, then run 1000 shots on Aer and compare.
