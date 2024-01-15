

def radix_sort(array, key: type=lambda x: x):
    l = [str(key(i)) for i in array]
    d = len(max(l))

    for i in range(1, d+1):
        array = count_sort(array, 9, i, key)

    return array


def count_sort(array, max, digit, key: type=lambda x: x):
    a, m = array, max
    c = [0 for i in range(m+1)] 
    b = [0 for i in range(len(array) + 1)]
    
    for i in range(len(a)):
        c[which_digit(key(a[i]), digit)] += 1
    
    for i in range(1, len(c)):
        c[i] += c[i-1]
    
    for i in range(len(a)-1, -1, -1):
        b[c[which_digit(key(a[i]), digit)]] = a[i]
        c[which_digit(key(a[i]), digit)] -= 1

    return b[1:]


def which_digit(integer, digit):
    base =  10 ** (digit)
    integer %= base
    base /= 10
    return int(integer // base)