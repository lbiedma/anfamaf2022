import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt("https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat")

x = datos[:, 0]
y = datos[:, 1]

# INCISO A
m = len(x)
a = 0
for idx in range(m):
    a = a + x[idx] ** 2

b = 0
for idx in range(m):
    b = b + y[idx]

c = 0
for idx in range(m):
    c = c + x[idx] * y[idx]

d = 0
for idx in range(m):
    d = d + x[idx]
# esto es lo mismo que d = x.sum()

a_0 = (a * b - c * d) / (m * a - d ** 2)
a_1 = (m * c - b * d) / (m * a - d ** 2)

# plt.plot(x, y, '*')
# plt.plot(x, a_1 * x + a_0)
# plt.title("inciso a")
# plt.show()

# INCISO B
unos = np.ones(m)
a = np.dot(x, x)
b = np.dot(y, unos)
c = np.dot(x, y)
d = np.dot(x, unos)

a_0 = (a * b - c * d) / (m * a - d ** 2)
a_1 = (m * c - b * d) / (m * a - d ** 2)

# plt.plot(x, y, '*')
# plt.plot(x, a_1 * x + a_0)
# plt.title("inciso b")
# plt.show()

# INCISO C
x = np.linspace(0, 10, 20)
y = 0.75 * x - 0.5
dispersion = np.random.randn(20)
puntos_con_ruido = y + dispersion

ajuste = np.polyfit(x, puntos_con_ruido, 1)
recta_ajustada = np.polyval(ajuste, x)

plt.plot(x, y, '*')
plt.plot(x, puntos_con_ruido, 'o')
plt.plot(x, recta_ajustada)
plt.show()
