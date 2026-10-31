def share(counts):
    total = counts['0'] + counts['1']
    return counts['0'] / total

print(share({'0': 510, '1': 490}))
print(share({'0': 484, '1': 516}))
