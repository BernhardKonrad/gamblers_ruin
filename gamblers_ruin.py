# Simulate gamblers ruin
from random import random

moneyA = 10
moneyB = moneyA

while moneyA > 0 and moneyB > 0:
    if random() < 0.5:
        moneyA += 1
        moneyB -= 1
    else:
        moneyA -= 1
        moneyB += 1

print moneyA, moneyB
