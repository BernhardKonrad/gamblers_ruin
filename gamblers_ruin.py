# Simulate gamblers ruin
from random import random

initial = 10
moneyA = [initial]

while moneyA[-1] > 0 and moneyA[-1] < 2 * initial:
    if random() < 0.5:
        moneyA.append(moneyA[-1] + 1)
    else:
        moneyA.append(moneyA[-1] - 1)

moneyB = [2 * initial - m for m in moneyA]
print moneyA, moneyB
