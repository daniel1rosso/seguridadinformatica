asignaturas = ['Análisis Matemático I', 'Física I', 'Física II', 'Redes de Información', 'Seguridad Informática']
notas = []
i = 0;
while i != len(asignaturas):
    nota = input("Introduce la nota de " + asignaturas[i] + " : ")
    notas.append(nota)
    i+=1

j = 0;
while j != len(asignaturas):
    print("En la asignatura " + asignaturas[j] + " ha sacado " + notas[j])
    j+=1