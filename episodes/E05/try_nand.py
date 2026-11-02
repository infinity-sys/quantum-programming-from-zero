# Possible answer to this episode's Try it yourself (shown in episode 5)
def NAND(a, b):
    return 1 - a * b

for a in [0, 1]:
    for b in [0, 1]:
        print(a, b, '|', NAND(a, b))
print(format(31, '05b'), 2 ** 5)
