from math import factorial  # Podemos usar el factorial de math
import matplotlib.pyplot as plt

### AUXILIAR: rbisec (esto puede ir en otro archivo y hacer import)
def rbisec(fun, I, mit, err):
    hx = []
    hf = []
    a, b = I

    u = fun(a)
    v = fun(b)

    if u * v > 0:
        print("no se cumplen las hipotesis")
        return None

    for it in range(mit):
        e = (b - a) / 2
        c = a + e
        w = fun(c)
        hx.append(c)
        hf.append(w)
        
        if abs(w) < err:
            break

        if w * v < 0:
            a = c
            u = w
        else:
            b = c
            v = w

    return hx, hf


### EJERCICIO 1
def serie_seno(x):
    s = 0
    for i in range(5):
        s += (-1)**i * x ** (2 * i + 1) / factorial(2 * i + 1)
    return s

### EJERCICIO 2
x = [i * 0.01 for i in range(641)]  # Podemos generar una lista de x entre 0 y 6.4, separados por 0.01
y = [serie_seno(xi) for xi in x]  # En este ejemplo xi toma el valor que esté dentro de x, o sea al principio sera 0 y luego 0.01 y asi...

plt.plot(x, y)
# Opcional: se puede agregar una línea horizontal en el 0 para ayudar a la visualización de raíces con axhline
plt.axhline(y=0.0, linestyle="--", color="black")
plt.show()

### EJERCICIO 3
# Se puede elegir los intervalos [2, 4] y [4, 6] mirando el gráfico.
error = 1e-5
iteraciones = 100
print("EJERCICIO 3")
hx, hf = rbisec(serie_seno, [2, 4], iteraciones, error)
print(f"rbisec llega a la raíz {hx[-1]} con {len(hx)} iteraciones.")
print("---------------------------------------")
hx, hf = rbisec(serie_seno, [4, 6], iteraciones, error)
print(f"rbisec llega a la raíz {hx[-1]} con {len(hx)} iteraciones.")
print("---------------------------------------")


### EJERCICIO 4
def steffensen(fun, x_0, err, mit):
    hx = [x_0]
    hf = [fun(x_0)]

    for i in range(mit):
        x_0 = x_0 - fun(x_0)**2 / (fun(x_0 + fun(x_0)) - fun(x_0))
        hx.append(x_0)
        hf.append(fun(x_0))
        if abs(fun(x_0)) < err:
            break
    
    return hx, hf

### EJERCICIO 5
error = 1e-5
iteraciones = 100
print("EJERCICIO 5")
hx, hf = steffensen(serie_seno, 3, error, iteraciones)
print(f"Para x_0 = 3, Steffensen llega a la raíz {hx[-1]} con {len(hx)} iteraciones.")
print("---------------------------------------")
hx, hf = steffensen(serie_seno, 6, error, iteraciones)
print(f"Para x_0 = 6, Steffensen llega a la raíz {hx[-1]} con {len(hx)} iteraciones.")
print("---------------------------------------")
hx, hf = steffensen(serie_seno, 4.5, error, iteraciones)
print(f"Para x_0 = 4.5, Steffensen se detiene por el máximo de iteraciones y llega al valor {hx[-1]}, pero la función allí vale {hf[-1]}, por lo tanto no converge el método.")
