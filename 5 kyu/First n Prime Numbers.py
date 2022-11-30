from gmpy2 import next_prime as np
class Primes:
    def first(n):
        a = []
        b = 1
        while len(a)<n:
            b = np(b)
            a += [b]
        return a