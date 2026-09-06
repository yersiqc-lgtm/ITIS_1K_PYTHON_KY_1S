# TASK 2 (НОВЫЕ ДОМАШНИЕ ЗАДАНИЕ)

import math
import matplotlib.pyplot as plt

G = 9.81
i = 0.1
final = 2
paso = 0.2

longitudes = []
periodos = []

while (i <= final):
    t = 2 * math.pi * math.sqrt(i / G)
    longitudes.append(round(i, 2))
    periodos.append(round(t, 4))
    print("{} -> {} ".format(round(i,2), round(t,4)), ", " if i < final-paso else "", end="")
    i += paso

plt.figure()
plt.plot(longitudes, periodos, marker='.', color='green')
plt.title("[Periodos]")
plt.xlabel("Longitud [L]")
plt.ylabel("Periodo [T]")
plt.grid(True)
plt.show()