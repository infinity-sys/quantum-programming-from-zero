# Magnitude and phase of a complex number
import cmath, math
for z in [1 + 0j, 1j, -1 + 0j, 1 + 1j]:
    r = abs(z)
    angle = math.degrees(cmath.phase(z))
    print(z, round(r, 4), round(angle, 1))
