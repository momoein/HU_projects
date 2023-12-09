import math
import numpy as np


Pc = 0.9
Pm = 0.005
N = 10
L = 16
gene_bits = 8
x1_lo = -4
x1_hi = 2
x2_lo = -1.5
x2_hi = 1

def initial_population(pop_size, chromozome_len):
    return np.random.choice([0, 1], (pop_size, chromozome_len))
    
    
pop = initial_population(N, L)
# print(pop)

def fit(x1, x2):
    return (1 + np.cos(2 * np.pi * x1 * x2)) * np.exp(-(np.absolute(x1) + np.absolute(x2))/2)


def normalize_chromozome(chromozome):
    x1 = chromozome[:8]
    x2 = chromozome[8:]

    # change base to 10
    for i in range(7):
        x1[i] = x1[i] * np.power(2, 7-i)
        x2[i] = x2[i] * np.power(2, 7-i)
    x1 = np.sum(x1)
    x2 = np.sum(x2)

    # normalize value
    x1n = x1 / (2**8 - 1)
    x2n = x2 / (2**8 - 1)

    return np.array([x1n, x2n])


def get_real_value(Xn):
    Xn[0] = x1_lo + Xn[0] * (x1_hi - x1_lo)
    Xn[1] = x2_lo + Xn[1] * (x2_hi - x2_lo)
    return Xn


def decode_pop(population):
    pop = []
    for chrom in population:
        normal = normalize_chromozome(chrom)
        pop.append(get_real_value(normal))
        
    return np.array(pop)



pop_decode = decode_pop(pop)
print(pop_decode)
for i in pop_decode:
    print(fit(i[0], i[1]))