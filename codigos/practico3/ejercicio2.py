def dif_divididas(x, y):
    n = len(x)
    coefs = []
    # Genero filas de coefs
    for i in range(n):
        coefs.append(y[:n - i].copy())
    
    # Calculo coeficientes de diferencias divididas
    for i in range(1, n):
        for j in range(n - i):
            (coefs[i])[j] = ((coefs[i-1])[j+1] - (coefs[i-1])[j])
            (coefs[i])[j] = (coefs[i])[j] / (x[j + i] - x[j])
    
    print(coefs)

    # Genero vector de coeficientes del polinomio
    c = [x[0] for x in coefs]
    return c

def test_dif_divididas():
    # Este es el conjunto de datos del teórico, debería darnos lo mismo.
    x = [3, 1, 5, 6]
    y = [1, -3, 2, 4]
    print(dif_divididas(x, y))

# Para poder terminar el ejercicio, es necesario generar la función
# inewton que calcule diferencias divididas y luego evalúe el polinomio
# con el esquema del teórico.

# def inewton(x, y, z):
#     c = dif_divididas(x, y)
#     for z; for c
