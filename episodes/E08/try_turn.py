# E07 task 2: multiply 1 + 1j by 1j
import cmath, math
z = 1 + 1j
w = z * 1j
print(w)
before = math.degrees(cmath.phase(z))
after = math.degrees(cmath.phase(w))
print(round(before, 1), round(after, 1))
