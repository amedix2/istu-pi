from math import isqrt

def is_prime(n: int) -> bool:
    """
    Проверяет, является ли число n простым.
    
    Простое число — это натуральное число больше 1, 
    у которого нет положительных делителей, кроме 1 и самого себя.
    
    Args:
        n (int): Число для проверки
        
    Returns:
        bool: True если число простое, False в противном случае
        
    Raises:
        TypeError: Если передан не целочисленный аргумент
    """
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
