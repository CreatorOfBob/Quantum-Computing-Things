import numpy as np, math
import random as r
def groverSearch(n):
    N = 2**n
    marked_index = r.randint(0, N-1)
    psi = np.ones(N, dtype=complex) / math.sqrt(N)
    iterations = int(np.floor((math.pi/4) * math.sqrt(N)))
    for i in range(iterations):
        psi[marked_index] *= -1
        mean = np.mean(psi)
        psi = 2*mean - psi 
    prob = abs(psi[marked_index])**2 
    return marked_index, prob
