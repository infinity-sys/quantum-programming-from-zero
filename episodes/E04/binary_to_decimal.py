# Each place is worth double the place on its right: 8 4 2 1
bits = '1011'
total = 1*8 + 0*4 + 1*2 + 1*1
print(total)
print(int(bits, 2))      # Python does the same
print(format(11, 'b'))   # and back again
print(2 ** 4, 2 ** 8)    # how many patterns 4 bits and 8 bits give
