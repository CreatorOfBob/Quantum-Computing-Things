import numpy as np, math
import random as r
n = 8
N = 2**n
marked_index = r.randint(0, N)
psi = np.ones(N, dtype=complex) / math.sqrt(N)
for i in range(int(np.floor((math.pi/4)*math.sqrt(N)))):
    psi[marked_index] *= -1
    mean = np.mean(psi)
    psi = 2*mean - psi
prob = abs(psi[marked_index])**2
print(f"n={n}, marked={marked_index}, success≈{prob}")
