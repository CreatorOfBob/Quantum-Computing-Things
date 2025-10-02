import numpy as np
import math
import random
from fractions import Fraction

# Parameters
N = 35

m = math.ceil(math.log2(N))
t = 2 * m
q = 1 << t
dim2 = 1 << m

print(f"Factoring N = {N}")
print(f"Quantum registers: {t} qubits (q={q}), {m} qubits (dim={dim2})\n")

attempts=0
while True:
    attempts+=1;
    a = random.randrange(2, N)
    g = math.gcd(a, N)
    print(f"Attempt {attempt}: a = {a}, gcd(a,N) = {g}")
    if 1 < g < N:
        print(f"  ✓ Found factor by gcd: {g} × {N//g}")
        break
    state = np.zeros((q, dim2), dtype=np.complex128)
    state[:, 1] = 1.0 / math.sqrt(q)
    for x in range(q):
        state[x, :] = 0
        state[x, pow(a, x, N)] = 1.0 / math.sqrt(q)
    state = np.fft.fft(state, axis=0) / math.sqrt(q)
    probs = np.sum(np.abs(state)**2, axis=1)
    probs /= probs.sum()
    y = np.random.choice(q, p=probs)
    print(f"  Measured y = {y}")
    if y == 0:
        print("  y = 0 gives no info, retrying...")
        continue
    frac = Fraction(y, q).limit_denominator(N)
    r = frac.denominator  
    print(f"  Continued fraction: {y}/{q} ≈ {frac} → r = {r}")

    if r == 0 or pow(a, r, N) != 1:
        print("  r invalid (a^r ≠ 1 mod N), retrying...")
        continue
    
    if r % 2 == 1:
        print("  r is odd, retrying...")
        continue
  
    apow = pow(a, r // 2, N)
    if apow == N - 1:
        print("  a^(r/2) ≡ -1 mod N, unlucky, retrying...")
        continue
    
    f1 = math.gcd(apow - 1, N)
    f2 = math.gcd(apow + 1, N)
    
    if 1 < f1 < N:
        print(f"  ✓ Success! Factors: {f1} × {N//f1}")
        break
    
    if 1 < f2 < N:
        print(f"  ✓ Success! Factors: {f2} × {N//f2}")
        break
