# Multiplying by i turns a quarter circle
z = 1 + 0j
for step in range(4):
    z = z * 1j
    print(step + 1, z.real + 0, z.imag + 0)
