# Adding two bits with two gates: XOR gives the sum, AND gives the carry
def half_adder(a, b):
    total = (a + b) % 2      # XOR
    carry = a * b            # AND
    return carry, total

for a in [0, 1]:
    for b in [0, 1]:
        carry, total = half_adder(a, b)
        print(a, '+', b, '=', str(carry) + str(total))
