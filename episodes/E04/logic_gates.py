# The four classical logic gates, as Python functions
def NOT(a):
    return 1 - a

def AND(a, b):
    return a * b

def OR(a, b):
    return max(a, b)

def XOR(a, b):
    return (a + b) % 2

print('a | NOT')
for a in [0, 1]:
    print(a, '|', NOT(a))

print('a b | AND OR XOR')
for a in [0, 1]:
    for b in [0, 1]:
        print(a, b, '|', AND(a, b), ' ', OR(a, b), ' ', XOR(a, b))
