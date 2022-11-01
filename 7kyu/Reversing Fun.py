def reverse_fun(n):
    list1 = []
    list2 = list(n)

    i = len(list2)
    while i > 0:
        list2 = list2[::-1]
        list1.append(list2.pop(0))
        i -= 1

    return "".join(list1)


reverse_fun("012345")
reverse_fun("jointhedarkside")