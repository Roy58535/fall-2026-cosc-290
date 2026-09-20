import numpy as np
import secrets
import sys

def fast_mod_exp(x:int, y:int, m:int) -> int:
    if y == 1:
        return x % m
    r = fast_mod_exp(x, y // 2, m)
    if y % 2 != 0:
        return x * r ** 2 % m
    else:
        return r ** 2 % m

def flt_test(n:int) -> bool:
    for i in range(20):
        a = secrets.randbelow(n - 1) + 1
        if fast_mod_exp(a, n, n) != a:
            return False
    return True

def find_prime_q(digits:int=5) -> tuple[int, int]:
    min_q = 10 ** (digits - 1)
    q = secrets.randbelow(10 ** digits - min_q) + min_q
    while q % 2 == 0 or not flt_test(q):
        q = secrets.randbelow(10 ** digits - min_q) + min_q
    return q

def make_dh_parameters(digits:int) -> tuple[int, int]:
    q = find_prime_q(digits)
    n = 2 * q + 1
    while not flt_test(n):
        q = find_prime_q(digits)
        n = 2 * q + 1

    g = secrets.randbelow(n - 3) + 2
    while fast_mod_exp(g, q, n) == 1:
        g = secrets.randbelow(n - 3) + 2

    return (n, g)

def main() -> None:
    usage = f"Usage: python3 {sys.argv[0]} <digits>   (digits >= 2)"
    if len(sys.argv) != 2:
        print(usage, file=sys.stderr)
        sys.exit(1)
    try:
        digits = int(sys.argv[1])
    except ValueError:
        print(usage, file=sys.stderr)
        print(f"  {sys.argv[1]!r} is not an integer", file=sys.stderr)
        sys.exit(1)
    if digits < 2:
        print(usage, file=sys.stderr)
        sys.exit(1)

    n, g = make_dh_parameters(digits)
    print(f"n {n}")
    print(f"g {g}")

if __name__ == "__main__":
    main()