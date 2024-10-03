#!/usr/bin/python3
"""
This module contains the solution for the Prime Game problem.
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game for multiple rounds.
    """
    def sieve_of_eratosthenes(n):
        """
        Generate a list of prime numbers up to n using the Sieve of Eratosthenes.
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    def play_game(n):
        """
        Simulate a single game of the Prime Game.
        """
        primes = sieve_of_eratosthenes(n)
        prime_count = sum(primes)
        return prime_count % 2 == 1  # Maria wins if there are an odd number of primes

    if not nums or x != len(nums):
        return None

    maria_wins = sum(play_game(n) for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
