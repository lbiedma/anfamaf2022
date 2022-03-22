import math

a = 1.0

for idx in range(10000):
    a = a / 2.0
    print(a)
    if a == 0.0:
        print(-idx)
        break

a = 1.0

for idx in range(10000):
    a = a * 2.0
    print(a)
    if math.isinf(a):
        print(idx)
        break

a = 1.0
contador = 0
while (math.isinf(a) == False):
    a = a * 2.0
    contador = contador + 1
    print(a)
print(contador)
