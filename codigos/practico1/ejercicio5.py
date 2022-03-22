# ejercicio a
print(1 * 2 * 3 * 4 * 5 * 6)

# ejercicio b
import math
print(math.factorial(6))

# ejercicio c
def nuestro_factorial(n):
    resultado = 1
    for multiplicador in range(1, n + 1):
        resultado = resultado * multiplicador

    return resultado

resultado_inciso_c = nuestro_factorial(6)
print(resultado_inciso_c)
