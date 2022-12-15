#https://www.codewars.com/kata/5e4de3b05d0b5f0022501d5b

from string import digits as d, ascii_uppercase as u, ascii_lowercase as l

def next_num(b, n, s=d+u+l):
    digits = {d: i for i, d in enumerate(s[:b])}
    nxt, n = False, [s[0]] + list(n)
    inc, ptr, x = False, 1, 0
    while 0 <= ptr < len(n):
        p = ptr + (ptr == 0 or n[0] > s[0])
        inc |= ptr == len(n)-1 and nxt == False
        d = (x*b%p + digits[n[ptr]] + inc + p-1) // p * p - x*b%p
        if d >= b:
            inc, ptr, x = True, ptr - 1, x // b
            continue
        if d > digits[n[ptr]]:
            nxt, n[ptr:] = True, [s[d]] + [s[0]] * (len(n) - ptr - 1)
        inc, ptr, x = False, ptr + 1, x*b + d
    if ptr >= 0:
        return ''.join(n).lstrip(s[0])