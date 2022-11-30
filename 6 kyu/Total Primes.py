import math, re
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def get_total_primes(a, b):
    c = 0
    while a < b:
        r = re.search('[014689]', str(a)[::-1])
        if r:
            a += 10**r.start()
            a -= a % 10**r.start()
            continue
        if is_prime(a):
            c += is_prime(a)
        a += 1
    return c