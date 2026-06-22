def p16(a, b):
    r = []
    for i in (a):
        f = True
        for j in b:
            if i == j:
                f = False
        if f:
            r += [i]
    return print(r)
s1 = p16([4, 5, 3], [2, 5, 1, 4])
s2 = p16([2, 5, 1, 4], [4, 5, 3])