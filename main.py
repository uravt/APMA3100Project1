import random
import pandas as pd
import matplotlib.pyplot as plt

alpha = 0.1

def run_iteration():
    prob = p
    cycle = 1
    while True:
        rand_val = random.uniform(0, 1)
        print(rand_val)
        
        if rand_val <= prob:
            print(cycle)
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

    total = 0
    counts = df["X"].value_counts().sort_index()  # Series indexed by X value
    print("p: "+str(p))
    print("\nCounts by realization value (X):")
    for x_val, cnt in counts.items():
        print(f"X = {x_val}: {cnt}")
        total += x_val * cnt
    print(f"\nExpected Value E[X]: {total / len(df)}")

    # histogram of results
    plt.hist(df["X"], bins=20)
    plt.xlabel("Realization Value (X)")
    plt.ylabel("Frequency")
    plt.title("Histogram of Realization Values (X)")
    plt.show()