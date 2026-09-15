import numpy as np
import random
import secrets

def fast_mod_exp(x:int, y:int, m:int) -> int:
    if y == 1:
        return x % m
    r = fast_mod_exp(x, y // 2, m)
    if y % 2 != 0:
        return x * r ** 2 % m
    else:
        return r ** 2 % m

def hack_dh_key(g:int, n:int, A:int, B:int) -> int:
    r_a = 0
    a = 1
    while r_a != A:
        r_a = fast_mod_exp(3, a, n)
        a += 1

    return fast_mod_exp(B, a - 1, n)

def flt_test(n:int) -> bool:
    for i in range(20):
        a = secrets.randbelow(n - 1) + 1
        # print(f"a = {a}, flt = {fast_mod_exp(a, n, n)}")
        if fast_mod_exp(a, n, n) != a:
            return False
    return True

def count_remainders(g:int, n:int) -> int:
    remainders = []
    for a in range(1, n + 1):
        remainders.append(fast_mod_exp(g, a, n))
    return len(set(remainders))

def find_g_n() -> tuple[int, int]:
    n = secrets.randbelow(899) + 100
    while n % 2 == 0 or not flt_test(n):
        n = secrets.randbelow(899) + 100
    for g in range(1, n):
        if count_remainders(g, n) == n - 1:
            return (g, n)
    return (0, 0)

def find_large_g_n() -> tuple[int, int]:
    q = find_prime_q()
    n = 2 * q + 1
    while not flt_test(n):
        q = find_prime_q()
        n = 2 * q + 1

    g = secrets.randbelow(n - 4) + 2
    while fast_mod_exp(g, 2, n) == 1:
        g = secrets.randbelow(n - 4) + 2

    return (g, n)

def find_prime_q() -> tuple[int, int]:
    q = secrets.randbelow(10000) + 10000
    while q % 2 == 0 or not flt_test(q):
        q = secrets.randbelow(10000) + 10000
    return q
    

print(fast_mod_exp(10, 157, 2026))
print(hack_dh_key(3, 31, 11, 17))
# print(hack_dh_key(1380889579903879951, 12241706495108194253, 5697403814009845641, 10857110447958648793))

print(f"Is 12241706495108194253 prime? {flt_test(12241706495108194253)}")
print(f"Is 9963569738995424389 prime? {flt_test(9963569738995424389)}")
print(f"Is 9237750053364305929 prime? {flt_test(9237750053364305929)}")

print(count_remainders(2, 13))
print(find_g_n())
g, n = find_large_g_n()
print(f"g = {g}, n = {n}")
print(count_remainders(g, n))