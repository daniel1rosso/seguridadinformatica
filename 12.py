diccionario = {'Seguridad Informática': 0, 'Desarrollo Web': 0, 'Redes Avanzadas': 0}
creditos = 0

for key in diccionario:
    diccionario[key] = input("Introducir el credito de " + key + " : ")

for key in diccionario:
    print("La asignatura " + key + " tiene " + diccionario[key] + " creditos.")
    creditos += int(diccionario[key])

print("Total de creditos: " + str(creditos))