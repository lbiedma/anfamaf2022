import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

from ejercicio1 import ilagrange

x = [1, 2, 3, 4, 5]
y = [1, 1/2, 1/3, 1/4, 1/5]

# Podemos usar la función linspace de la librería NumPy para generar 101 puntos entre 1 y 5
z = np.linspace(1, 5, 101)
# Lo bueno de contar con un arreglo de NumPy es que podemos hacerle operaciones aritméticas
# simples a todo el objeto, como obtener el inverso (1 / z)
f_z = 1 / z

# Calculo el polinomio de lagrange en z
w = ilagrange(x, y, z)

# Scipy, para poder usar Spline es necesario agregar el argumento kind="cubic"
# interp1d nos devuelve una función que podemos evaluar
polinomio = interp1d(x, y, kind="cubic")
spline_puntos = polinomio(z)

plt.plot(z, f_z, label="f(z)")
plt.plot(z, w, label="p(z)")
plt.plot(z, spline_puntos, label="spline(z)")
plt.plot(x, y, "*", label="puntos")
plt.legend()
plt.show()
