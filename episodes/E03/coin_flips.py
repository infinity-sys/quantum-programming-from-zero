import random

random.seed(2026)        # same results every run
counts = {'0': 0, '1': 0}

for shot in range(1000):
    bit = random.choice(['0', '1'])
    counts[bit] = counts[bit] + 1

print(counts)
