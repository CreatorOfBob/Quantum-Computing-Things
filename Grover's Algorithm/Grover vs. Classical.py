import numpy as np, math
import matplotlib.pyplot as plt
max_n = 12
ns = np.arange(2, max_n + 1)
N_vals = 2**ns
classical_avg = N_vals / 2
classical_worst = N_vals
grover_iters = []
grover_probs = []
for N in N_vals:
    marked_index = np.random.randint(0, N)
    psi = np.ones(N, dtype=complex) / math.sqrt(N)
    iterations = int(np.floor((math.pi / 4) * np.sqrt(N)))
    for I in range(iterations):
        psi[marked_index] *= -1
        psi = 2 * np.mean(psi) - psi
    prob = abs(psi[marked_index])**2
    grover_iters.append(iterations)
    grover_probs.append(prob)
    print(f"N={N}, Grover iters={iterations}, success≈{prob:.5f}, "
          f"Classical avg={N/2}, worst={N}")

# Plots
plt.figure(figsize=(7,5))
plt.plot(N_vals, classical_avg, "o-", label="Classical avg checks")
plt.plot(N_vals, classical_worst, "o--", label="Classical worst-case")
plt.plot(N_vals, grover_iters, "s-", label="Grover iterations")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Search space size N = 2^n")
plt.ylabel("Steps / Checks")
plt.title("Grover’s Algorithm vs Classical Search")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()
