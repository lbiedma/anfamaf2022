def horn(coefs, x):
    """
    Función que calcula el valor del polinomio cuyos coeficientes son parte de la lista
    coefs y devuelve como resultado la evaluación del polinomio en x.

    Por ejemplo, coefs = [1, 2, -3] -> x**2 + 2 * x - 3
    y horn([1, 2, -3], 2.0) = 5.
    """

    # Primero, obtenemos la longitud de la lista, para poder iterar sobre ella.
    n = len(coefs)
    # Definimos la variable b, que será la de salida, como el primer coeficiente.
    b = coefs[0]
    for idx in range(1, n):
        # Iteramos desde el segundo elemento de coefs hasta el último
        # siguiendo la fórmula del teórico
        b = coefs[idx] + x * b
    
    return b

# Finalmente probamos la función, este resultado debería ser 2.
p = horn([1, -5, 6, 2], 2)
print(p)
