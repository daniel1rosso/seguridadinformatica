import statistics as stats

ingreso = input("Introduce numeros separados por ; y luego se le dara la media y la desviación típica : ")
ingreso_array = ingreso.split(sep=';')
for i in range(len(ingreso_array)):
    ingreso_array[i] = int(ingreso_array[i])
print(ingreso_array)

media = stats.mean(ingreso_array)
print("La media es : " + str(media))

desviacion = stats.pstdev(ingreso_array)
print("La desviacion es : " + str(desviacion))