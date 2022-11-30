import bisect

polydivisible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
stack = list(polydivisible)
n = 2
while stack:
    temp = stack.pop(0)
    n = len(str(temp))
    for i in range(10):
        if (temp * 10 + i) % (n+1) == 0:
            polydivisible.append(temp * 10 + i)
            stack.append(temp * 10 + i)

def next_num(n):
    indx = bisect.bisect(polydivisible, n)
    return None if indx >= len(polydivisible) else polydivisible[indx]