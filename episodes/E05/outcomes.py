# Outcomes and their probabilities
coin = {'heads': 0.5, 'tails': 0.5}
die = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
print(sum(coin.values()))
print(sum(die.values()))
even = die[2] + die[4] + die[6]
print(even)
