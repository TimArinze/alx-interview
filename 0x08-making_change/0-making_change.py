#!/usr/bin/python3
"""
Making change
"""


def makeChange(coins, total):
    """Return 0 if total is 0 and -1 if any number of coins cant make change
    return the minimum number of coin needed to make change
    """
    if total is None:
        return 0
