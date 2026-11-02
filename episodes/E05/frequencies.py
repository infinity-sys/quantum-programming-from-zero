# Flip a fair coin many times, and count the zeros
import random
random.seed(2026)
for shots in [10, 100, 1000, 10000]:
    zeros = 0
    for i in range(shots):
        if random.randint(0, 1) == 0:
            zeros = zeros + 1
    print(shots, zeros, zeros / shots)
