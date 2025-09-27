import numpy as np, math
n = 4
marked_index = 2
N = 2**n
iterations = int(np.floor((math.pi/4)*math.sqrt(N)))
O = np.eye(N, dtype=complex)
O[marked_index, marked_index] = -1
s = np.ones((N,)) / math.sqrt(N)
D = 2*np.outer(s, s) - np.eye(N, dtype=complex)
psi = np.ones((N,), dtype=complex) / math.sqrt(N)
for _ in range(iterations):
    psi = O @ psi
    psi = D @ psi
print("Final state amplitudes:")
for i, amp in enumerate(psi):
    print(f"|{i:0{n}b}> : {amp.real:.3f}{amp.imag:+.3f}j, prob={abs(amp)**2}")
