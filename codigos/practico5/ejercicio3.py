import math
import matplotlib.pyplot as plt
import numpy as np

from ejercicio1 import intenumcomp

def senint(x):
    N = math.ceil(x / 0.1) # np.ceil nos puede devolver un flotante (OJO)
    # if N % 2 == 1: # para PM o Simpson necesito N par
    #     N = N + 1

    return intenumcomp(math.cos, 0, x, N, 'trapecio')

x = np.arange(0, 2 * np.pi, 0.5)
y = np.sin(x)
y_aprox = []

for xi in x:
    y_aprox.append(senint(xi))

plt.plot(x, y, label='seno')
plt.plot(x, y_aprox, label='senint')
plt.legend()
plt.show()
