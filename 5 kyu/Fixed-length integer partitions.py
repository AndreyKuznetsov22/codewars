def indices(n, d):
    arr = [[[], d], ]
    for _ in range(n-1):
        temp = []
        for a, r in arr:
            for i in range(r+1):
                temp.append([a+[i], r-i])
        arr = temp
    return [x[0]+[x[1]] for x in arr]