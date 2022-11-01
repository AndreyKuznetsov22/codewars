def even_chars(st): 
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    else:
        return list(st[1::2])