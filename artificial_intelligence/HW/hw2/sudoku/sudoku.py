import numpy as np
import time
from csp import *


# ___ problem modeling ___

def var_tuple(variable: str):
    return tuple([int(i) for i in variable.split("-")])

def variable_neighbors(variable:str, variables):
    i, j = var_tuple(variable)
    neighbors = []
    for v in variables:
        vi, vj = var_tuple(v)
        if v not in neighbors and (v != variable):
            if (vi == i or vj == j) or ((i) // 3 == (vi) // 3) and ((j) // 3 == (vj) // 3):
                neighbors.append(v)    
    return neighbors
        
def parse_neighbors(variables):
    neighbors = {}
    for var in variables:
        neighbors[var] = variable_neighbors(var, variables)
    return neighbors

def different_values_constraint(A, a, B, b):
    return a != b


def SudokuCSP(variables, domains):
    neighbors = parse_neighbors(variables)
    return CSP(variables, domains, neighbors, different_values_constraint)


# ___ problem parameters ___

variables = [f"{i}-{j}" for i in range(9) for j in range(9)]

domains = {}
for var in variables:
    domains[var] = list("123456789")

# assignment = {
#     "0-0": "5", "0-1": "3", "0-4": "7", 
#     "1-0": "6", "1-3": "1", "1-4": "9", "1-5": "5",
#     "2-1": "9", "2-2": "8", "2-7": "6", "3-0": "8", "3-4": "6", "3-8": "3",
#     "4-0": "4", "4-3": "8", "4-5": "3", "4-8": "1",
#     "5-0": "7", "5-4": "2", "5-8": "6",
#     "6-6": "2", "6-7": "8",
#     "7-3": "4", "7-4": "1", "7-5": "9", "7-8": "5",
#     "8-4": "8", "8-7": "7","8-8": "9",
# }

assignment = {
    "0-6": "4", "0-8": "5", 
    "1-2": "1", "1-3": "9",
    "2-7": "6",
    "3-3": "8", "3-6": "9",
    "4-0": "7", "4-1": "5",
    "5-1": "6",
    "6-0": "2", "6-5": "4", "6-6": "3",
    "7-4": "7", "7-5": "5",
    "8-2": "9", "8-4": "6",
}

sudoku = SudokuCSP(variables, domains)
t1 = time.time()
result = backtracking_search(sudoku, assignment, mrv, unordered_domain_values, forward_checking, probability=0.1)

if result:
    table = np.zeros(shape=(9,9), dtype=str)
    for var in result:
        i, j = var_tuple(var)
        table[i, j] = result[var]
    print(table)
t2 = time.time()
print(f"took {round(t2-t1, 3)} secconds")