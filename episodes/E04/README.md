# E04: Bits, Binary and Logic Gates

Video: https://youtu.be/Roe_OE_MLyY

## E03 solution
1. `try_10000.py`: `range(10000)` gives `{'0': 4960, '1': 5040}` with seed 2026.
2. `try_seeds.py`: seeds 1, 7 and 42 give 485, 511 and 486 zeros out of 1000: always close to one half.
3. `try_share.py`: `share({'0': 510, '1': 490})` is `0.51`; `share({'0': 484, '1': 516})` is `0.484`.

## This episode
Plain Python, no Qiskit needed. Each program has its real output next to it (`.out`):
```
python episodes/E04/count_binary.py        # 0 to 15 in binary, with format(n, '04b')
python episodes/E04/binary_to_decimal.py   # 1011 = 8 + 2 + 1 = 11, int('1011', 2), 2 ** 4 and 2 ** 8
python episodes/E04/logic_gates.py         # NOT, AND, OR, XOR and their truth tables
python episodes/E04/half_adder.py          # XOR gives the sum, AND gives the carry: 1 + 1 = 10
```

## Your turn (solution in E05)
1. Count from 0 to 31 in binary. How many places do you need? What does 31 look like?
2. How many patterns can 5 bits make? Check with `2 ** 5`.
3. Write `NAND(a, b)` (not and) and print its truth table with two loops. Hint: build it from NOT and AND.
