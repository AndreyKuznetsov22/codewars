from itertools import combinations
from math import gcd

def first(n):
    n = str(n)
    return sum(sum(int(''.join(g)) for g in combinations(n,i)) for i in range(1,len(n)+1))

def second(n):
    n = str(n)
    return sum(sum(int(n[i:i+j]) for i in range(len(n)-j+1)) for j in range(1,len(n)+1))

def factors(n):
    return 1+sum(n%i==0 for i in range(2,n//2+1))

def find_int_inrange(a, b):
    d = {}
    for i in range(a, b):
        x = factors(gcd(first(i),second(i)))
        if x>3:
            if x in d:
                d[x] += [i]
            else:
                d[x] = [i]
    res = [max(d)]
    return res+[i for i in d[max(d)]]