from ejercicio3 import rnewton

"encontrar la raiz cubica de a"

def buscar_raiz_cubica(a):
    fun = lambda x: (x ** 3 - a, 3 * x ** 2)
    """
    lo de arriba es lo mismo que hacer lo siguiente (adentro de la funcion!!!)
    def fun(x):
        return x ** 3 - a, 3 * x ** 2
    """
    hx, hf = rnewton(fun, a, 1e-8, 100)
    return hx, hf

hx, hf = buscar_raiz_cubica(27.0)
print(hx[-1])
