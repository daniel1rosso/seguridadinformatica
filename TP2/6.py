numero = int(input("Ingrese un numero y te dire si es primo: "))


for n in range(2, numero):
    if numero % n == 0:
        print("No es primo")
print("Es primo")
