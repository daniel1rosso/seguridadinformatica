frase2 = input("Introduce una frase: ")
letra_may = input("Introduce una letra a destacar: ")

def reemplazo(frase):
    i = 0

    while i < len(frase):
        if frase[i] == letra_may:
            frase = frase.replace(frase[i], letra_may.upper())
        i = i + 1
    return frase

print("Cadena modificada " + reemplazo(frase2) )