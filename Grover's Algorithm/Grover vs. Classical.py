import numpy as np, math
import matplotlib.pyplot as plt
max = 12
ns = list(range(2, max+1))
N_vals = [2**n for n in ns]
classical_avg = []
classical_worst = []
grover_iters = []
grover_probs = []
for n in ns:
    N = 2**n
    marked_index = np.random.randint(0, N)
    psi = np.ones(N, dtype=complex) / math.sqrt(N)
    iterations = int(np.floor((math.pi/4)*math.sqrt(N)))
    for _ in range(iterations):
        psi[marked_index] *= -1
        mean = np.mean(psi)
        psi = 2*mean - psi

    prob = abs(psi[marked_index])**2

    avg_checks = N/2
    worst_checks = N

    classical_avg.append(avg_checks)
    classical_worst.append(worst_checks)
    grover_iters.append(iterations)
    grover_probs.append(prob)

    print(f"n={n}, N={N}, Grover iters={iterations}, success≈{prob:.3f}, "
          f"Classical avg={avg_checks}, worst={worst_checks}")

#Plots#
plt.figure(figsize=(7,5))
plt.plot(N_vals, classical_avg, "o-", label="Classical avg checks")
plt.plot(N_vals, classical_worst, "o--", label="Classical worst-case")
plt.plot(N_vals, grover_iters, "s-", label="Grover iterations")
plt.xscale("log"); plt.yscale("log")
plt.xlabel("Search space size N = 2^n")
plt.ylabel("Steps / Checks")
plt.title("Grover’s Algorithm vs Classical Search")
plt.legend(); plt.grid(True, which="both", ls="--")
plt.tight_layout(); plt.show()
