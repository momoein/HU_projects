a = [1,2,3]

def power_set(array):
    if len(array) <= 1:
        return array
    n_th = array[-1]
    set = power_set(array[:-1])
    # creat power set for new list
    new = []
    for i in set:
        if type(i) is not list:
            new.append([i, n_th])
        else:
            new.append(i + [n_th])
    # combine old set and new set
    set = set + [n_th] + new
    return set

print(power_set(a))