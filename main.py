import random
import pandas as pd
import matplotlib.pyplot as plt

alpha = 0.1


def run_iteration():
    prob = p
    cycle = 1
    while True:
        rand_val = random.uniform(0, 1)
        if rand_val <= prob:
            return cycle
        else:
            prob = min(1, prob + (cycle - 1) * alpha)
            cycle += 1


def generate_trials():
    trials = []
    for i in range(10000):
        trials.append({"Trial": i, "X": run_iteration()})

    pd.DataFrame(trials).to_csv("output_p="+str(p)+".csv", index=False)

for p in [0.1, 0.2, 0.3, 0.4, 0.5]:
    generate_trials()
    df = pd.read_csv("output_p="+str(p)+".csv")


# histogram of results
plt.hist(df["X"], bins=20)
plt.xlabel("Trial Result")
plt.ylabel("Frequency")
plt.title("X")
plt.show()