from math import isqrt

def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = isqrt(n) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True
