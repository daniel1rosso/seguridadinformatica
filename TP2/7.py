frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra para buscar: ")

contar = frase.count(letra)
vez = 0
if contar == 1:
    vez = " vez"
else:
    vez = " veces"

print("La letra " + letra + " aparece "+ str(contar) + vez)