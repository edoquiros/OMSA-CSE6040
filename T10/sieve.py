from math import sqrt
import numpy as np


def sieve(n):
    """
    Returns the prime number 'sieve' shown above.

    That is, this function returns an array `X[0:n+1]`
    such that `X[i]` is true if and only if `i` is prime.
    """
    is_prime = np.empty(n + 1, dtype=bool)  # the "sieve"

    # Initial values
    is_prime[0:2] = False  # {0, 1} are _not_ considered prime
    is_prime[2:] = True  # All other values might be prime

    # Implement the sieving loop
    for i in range(2, int(sqrt(n))):
        x = np.arange(n + 1)
        is_prime = is_prime & ((x == i) | (x % i != 0))
    return is_prime


# Prints your primes
print("==> Primes through 20:\n", np.nonzero(sieve(20))[0])