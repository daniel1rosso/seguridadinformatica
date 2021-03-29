text = "01234567;Marcelo Lopez;mlopez@mail.com;12345678;12.5\n324234234;Milagros Ramírez;mramirez@mail.com;5556334535;8\n234234234;Juan Garcia;jgarcia@mail.com;664833232;5.2\n123123123;Diego Sánchez;dsanchez@mail.com;6634225;15.7"
diccionario = {}

for key in text.split(sep='\n'):
    subarray = key.split(sep=';')
    diccionario[subarray[0]] = {'nombre': subarray[1], 'email': subarray[2], 'teléfono': subarray[3], 'descuento': subarray[4]}

print(diccionario)
