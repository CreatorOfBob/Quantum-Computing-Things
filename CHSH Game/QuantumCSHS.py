import math
import random as r
def quantumMeasurement(Alice, Bob):
    optimalProb = (1+math.sqrt(2)/2)/2
    needCorrelation = (Alice == 0 and Bob == 0)
    if r.random() < optimalProb:
        if needCorrelation:
            a = b = r.randint(0, 1)
        else:
            a = r.randint(0, 1)
            b = 1-a
    else:
        if needCorrelation:
            a = r.randint(0, 1)
            b = 1-a
        else:
            a = b = r.randint(0, 1)
    return (a << 1) | b
rounds, wins = int(1e6), 0
for i in range(rounds):
    Alice, Bob = r.randint(0, 1), r.randint(0, 1)
    packed = quantumMeasurement(Alice, Bob)
    a, b = (packed >> 1) & 1, packed & 1
    if (a^b) == (Alice | Bob):
        wins+=1
print(f"Wins: {wins}, Losses: {rounds-wins}")
print(f"Win Percentage: {wins/rounds*100:}%")
