def multiplo(m, n):
    """
    Función que toma dos números y nos dice
    si el segundo es múltiplo del primero.
    Devuelve True si lo es, False si no.
    """
    if m % n == 0:
        print("es multiplo")
        return True
    else:
        print("no es multiplo")
        return False

# un caso que sí
print(multiplo(8, 4))

# un caso que no
print(multiplo(6, 5))
