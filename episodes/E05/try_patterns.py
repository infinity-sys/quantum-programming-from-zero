# Episode 4, task 2: how many patterns can 5 bits make?
patterns = 1
for bit in range(5):
    patterns = patterns * 2   # each extra bit doubles
    print(bit + 1, 'bits:', patterns)
print(2 ** 5)
