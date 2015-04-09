# Simulate gamblers ruin
from random import random


def simulate_one(initial, successA):
    '''
    Simulates gambler's ruin with
        two players,
        equal initial condition,
        fixed success rate,
        fixed bet size (1 unit)

    pre:
        initial: initial starting bankroll for either player.
        successA: (constant) success rate for player A at each turn.

    post:
        winner: 1 if player A wins, 0 otherwise
        moneyA: history of bankroll of player A (list)
        moneyB: history of bankroll of player B (list)
    '''

    #Bananas
    # BANANANANA
    moneyA = [initial]

    while moneyA[-1] > 0 and moneyA[-1] < 2 * initial:
        if random() < successA:
            moneyA.append(moneyA[-1] + 1)
        else:
            moneyA.append(moneyA[-1] - 1)

    moneyB = [2 * initial - m for m in moneyA]
    if moneyA[-1] > 0:
        winner = 1
    else:
        winner = 0

    return winner, moneyA, moneyB

print(simulate_one(5, 0.5))
print(simulate_one(10, 0.1))
