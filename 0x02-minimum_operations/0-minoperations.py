#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in a text file,
    where the only allowed operations are "Copy All" and "Paste".
    """
    if n <= 1:
        return 0

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
