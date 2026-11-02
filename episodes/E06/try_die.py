# E05 tasks 2 and 3: roll a die 6000 times
import random
random.seed(2026)
counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(6000):
    face = random.randint(1, 6)
    counts[face] = counts[face] + 1
print(counts)
even = counts[2] + counts[4] + counts[6]
print(even, even / 6000)
