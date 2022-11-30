def order(s):
    arr = []
    for i in range(1,10):
        for j in list(s.split()):
            if str(i) in j:
               arr.append(j)
    return " ".join(arr)