import random

import pandas
import pandas as pd

p = 0.3
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


trials = []
for i in range(10000):
    trials.append({"Trial": i, "X": run_iteration()})

pd.DataFrame(trials).to_csv("output.csv", index=False)

