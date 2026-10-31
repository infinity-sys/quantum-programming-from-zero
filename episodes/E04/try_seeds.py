import random

for seed in [1, 7, 42]:
    random.seed(seed)
    counts = {'0': 0, '1': 0}
    for shot in range(1000):
        bit = random.choice(['0', '1'])
        counts[bit] = counts[bit] + 1
    print(seed, counts)
