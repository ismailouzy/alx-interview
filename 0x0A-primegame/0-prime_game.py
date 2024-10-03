#!/usr/bin/python3

def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_count(n):
    """Returns the count of prime numbers from 1 to n."""
    return [i for i in range(2, n + 1) if is_prime(i)]

def isWinner(x, nums):
    """Determines the overall winner after x rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = prime_count(n)
        turn = 0  # 0 for Maria, 1 for Ben

        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            turn ^= 1  # Switch turns

        if turn == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

