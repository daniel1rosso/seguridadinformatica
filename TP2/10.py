import numpy as np

vector1 = []
vector2 = []

print("Ingresar el vector 1 para fenar la carga es con la palabra reservada exit")
ingreso = input("Introduce: ")

if ingreso.lower() != "exit":
    vector1.append(ingreso)

while ingreso.lower() != "exit":
    ingreso = input("Introduce: ")
    if ingreso.lower() != "exit":
        vector1.append(ingreso)

print("Ingresar el vector 2 para fenar la carga es con la palabra reservada exit")
ingreso2 = input("Introduce: ")

if ingreso2.lower() != "exit":
    vector2.append(ingreso2)

while ingreso2.lower() != "exit":
    ingreso2 = input("Introduce: ")
    if ingreso2.lower() != "exit":
        vector2.append(ingreso2)

vector1 = np.asarray(vector1, dtype='float64')
vector2 = np.asarray(vector2, dtype='float64')

producto_escalar = np.array([vector1]) * np.array([vector2])
print("El producto escalar es: ")
print(producto_escalar)