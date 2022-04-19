from ejercicio1 import rbisec

from math import tan
import matplotlib.pyplot as plt

def fun_labej2a(x):
    return 2 * x - tan(x)

hx, hf = rbisec(
    fun_labej2a, [0.8, 1.4],
    mit=100, err=1e-5
)


# grafico de la funcion entre 0.8 y 1.4
x = [0.01 * i for i in range(80, 141)]
y = [fun_labej2a(0.01 * i) for i in range(80, 141)]
plt.plot(x, y)
plt.plot(hx, hf, '*')
plt.plot(hx[-1], hf[-1], 'ok')
plt.title("Puntos Visitados")
plt.show()
