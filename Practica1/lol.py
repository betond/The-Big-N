"""
    https://parzibyte.me/blog
"""


def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def maximo_comun_divisor_recursivo(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor_recursivo(b, a % b)


a = 20
b = 1
resultado = maximo_comun_divisor(a, b)
resultado_recursivo = maximo_comun_divisor_recursivo(a, b)
print(
    f"El Máximo común divisor de {a} y {b} es {resultado}. De manera recursiva, es {resultado_recursivo}")