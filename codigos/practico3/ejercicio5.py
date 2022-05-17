import numpy as np 
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 

# cargamos los datos desde la url
datos = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos_aeroCBA.dat')

# los datos que nos interesan son anios (primer columna) y temperatura (segunda columna)
year = datos[:,0]
temp = datos[:,1]

# seleccion pares con datos no faltantes
temp_int = temp[~np.isnan(temp)]
year_int = year[~np.isnan(temp)]

# polinomio interpolante
pol = interp1d(year_int, temp_int, kind='cubic', fill_value='extrapolate')

# pares de puntos interpolados
year_plot = np.arange(1957,2017)
temp_plot = pol(year_plot)

# graficos
plt.plot(year_int,temp_int,'o',label='datos')
plt.plot(year_plot,temp_plot,label='innterpolaciones y extrapolaciones')

plt.legend()
plt.show()