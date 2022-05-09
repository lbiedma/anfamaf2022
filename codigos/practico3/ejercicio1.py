def ilagrange(x, y, z):
    """
    Cálculo del polinomio de Lagrange dado por los puntos (x_i, y_i) en los puntos z_i.
    """
    n = len(x)
    w = []  # Generamos una lista vacía donde almacenamos p(z_k)
    for k in z:
        suma = 0
        for i in range(n):
            prod = 1  # Siempre que comenzamos una productoria, usar 1 para iniciar (neutro del producto)
            for j in range(n):
                if i != j:
                    prod = prod * (k - x[j]) / (x[i] - x[j])
            # Sumamos l_i(z_k) * y_i        
            suma = suma + prod * y[i]
        
        w.append(suma)
    
    return w

def test_ilagrange():
    x = [-2, 0, 2]
    y = [4, 0, 4]
    z = [-5, 1, 3]

    w = ilagrange(x, y, z)

# Ejecutar test_ilagrange debería devolvernos la lista [25, 1, 9]
# test_ilagrange()
