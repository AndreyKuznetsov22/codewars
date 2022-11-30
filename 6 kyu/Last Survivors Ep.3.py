def last_survivors(arr, nums):
    survivivors = list()
    i = 0
    for n in nums:
        m = n
        for r in arr[::-1]:
            if r[i] != " ":
                if m == 0:
                    survivivors.append(r[i])
                else:
                    m -= 1
        i += 1
    return "".join(survivivors)