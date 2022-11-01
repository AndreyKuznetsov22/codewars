import random

def random_case(x):
    x = list(x)
    for i in range(len(x) // 2):
        k = random.randint(1, len(x) - 1)
        if x[k].isupper():
            x[k] = x[k].lower()
        else:
            x[k] = x[k].upper()
    return ''.join(x)