# Simulate gamblers ruin
from random import random

moneyA = [10]
moneyB = [10]

while moneyA[-1] > 0 and moneyB[-1] > 0:
    if random() < 0.5:
        moneyA.append(moneyA[-1] + 1)
        moneyB.append(moneyB[-1] - 1)
    else:
        moneyA.append(moneyA[-1] - 1)
        moneyB.append(moneyB[-1] + 1)

print moneyA, moneyB
