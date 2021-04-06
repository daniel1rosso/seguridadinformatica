import json
from json import encoder

import requests
dolar = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
json_response = dolar.json()
precio_dolar= (json_response[0]['casa']['compra'].split(','))
precio_dolar_entero=float(precio_dolar[0])
precio_dolar_completo = precio_dolar_entero + float(precio_dolar[1])/1000


valor_usd = float(input('Introducir el valor del producto en dolares con sus decimmles correspondiente y te devolvemos el valor en pesos '))
print('El valor en pesos es: ' + str(valor_usd * precio_dolar_completo))
print('El valor entero es: : ' + str(int(round(valor_usd * precio_dolar_completo,0))))
print('El valor en decimales es: : ' + str( ( valor_usd * precio_dolar_completo) -int(round(valor_usd * precio_dolar_completo,2)) ))