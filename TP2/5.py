altura = 0
altura = int(input("Ingrese la altura del triangulo: "))

for i in range(altura):
    for x in range(altura):
        if x <= i:
            print("*", end = "")
        if x == i:
            print("")