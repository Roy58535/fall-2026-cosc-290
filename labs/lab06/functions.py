P = 11

def inverse(a):
    """ The inverse of a mod P. """
    return pow(a, P - 2, P)


def poly_eval(poly, x):
    """ The value of the polynomial at x, mod P. """
    result = 0
    for coefficient in poly:
        result = (result * x + coefficient) % P
    return result


def poly_mul(a, b):
    """ The product ab of the two given polynomials, mod P. """
    product = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            product[i + j] = (product[i + j] + ai * bj) % P
    return product