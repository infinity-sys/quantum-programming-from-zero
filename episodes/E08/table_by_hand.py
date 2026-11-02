# A 2 x 2 table times a column, by hand
M = [[2, 1],
     [0, 3]]
v = [1, 2]
top = M[0][0] * v[0] + M[0][1] * v[1]
bottom = M[1][0] * v[0] + M[1][1] * v[1]
print([top, bottom])
