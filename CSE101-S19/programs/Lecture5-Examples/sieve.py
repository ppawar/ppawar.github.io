# Implementation of the Sieve of Eratosthenes algorithm for
# finding prime numbers.

from math import *

def sift(k, a):
    for i in range(2*k, len(a), k):
        a[i] = None

def non_nulls(a):
    res = []
    for x in a:
        if x is not None:
            res.append(x)
    return res

def sieve(n):
    worksheet = [None, None] + list(range(2, n))
    for k in range(2, ceil(sqrt(n))):
        if worksheet[k] is not None:
            sift(k, worksheet)

    return non_nulls(worksheet)

primes = sieve(50)
print(primes)
