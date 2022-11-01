def _all(seq, fun):
    for x in seq:
        if not x in filter(fun, seq):
            return False
    return True