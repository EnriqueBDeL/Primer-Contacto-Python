# !pip install requests

import requests as req

ciudad = input("Nombre de la ciudad de la que deseas saber el tiempo: ")

url = "https://wttr.in/" + ciudad + "?format=j1"


respuesta = req.get(url, verify=False)


datos = respuesta.json()

temperatura = datos["current_condition"][0]["temp_C"]


print(f"La temperatura en {ciudad} es de {temperatura} grados.")
