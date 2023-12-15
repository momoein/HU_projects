def basketball(n, r):
    if r+1 > n:
        return 1
    else:
        t1 = basketball(n, r+1)

    if r+2 <= n:
        t2 = basketball(n, r+2)
    else:
        t2 = 0

    if r+3 <= n:
        t3 = basketball(n, r+3)
    else:
        t3 = 0

    return t1 + t2 + t3


print(basketball(3, 0))