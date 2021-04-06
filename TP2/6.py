numero = int(input("Ingrese un numero y te dire si es primo: "))

def es_primo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo")
        return False

es_primo(numero)