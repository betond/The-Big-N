"""
    https://parzibyte.me/blog



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




"""



# Programa Python # para el algoritmo euclidiano extendido
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
 
 
if __name__ == '__main__':
 
   gcd, x, y = extended_gcd(26, 3)
   print('The GCD is', gcd)
   print(f'x = {x}, y = {y}')
   print("#$####################################################")
 