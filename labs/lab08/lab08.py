from math import factorial
import numpy as np

def fpf(n:int) -> int:
    """Returns the number of FPF permutations in all permutations of n"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return (n - 1) * (fpf(n - 1) + fpf(n - 2))

def p_fpf(n:int) -> float:
    return fpf(n) / factorial(n)

def fpf_iterative(n:int) -> int:
    fpf = np.zeros(n, dtype=object)
    fpf[1] = 1
    for i in range(2, n):
        fpf[i] = i * (fpf[i - 1] + fpf[i - 2])
    return fpf[n - 1]
    

# print(p_fpf(13))
print(fpf_iterative(7))