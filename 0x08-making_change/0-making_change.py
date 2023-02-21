#!/usr/bin/python3
""" Make change on Coins."""


def makeChange(coins, total):
    """ Implementation of the make change."""
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total == 0:
        return count
    else:
        return -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
