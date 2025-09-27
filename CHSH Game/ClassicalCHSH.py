import random as r
rounds, wins = int(1e6), 0
for i in range(rounds):
    Alice, Bob = r.randint(0,1), r.randint(0,1)
    if Alice==Bob==0:
        wins+=1
    elif Alice != Bob:
        wins+=1
print(f"Wins: {wins}, Losses: {rounds-wins}")
print(f"Win Percentage: {wins/rounds*100:}%")
