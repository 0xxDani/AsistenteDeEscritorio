'''AQUÍ TENEMOS UNA PÁGINA BÁSICA QUE NOS MUESTRA LA INFO DEL CLIMA EN UN FORMATO TIPO CODE MUY COOL HOHOH🦉,
CON WEB BROWSER HACEMOS LA BUSQUEDA SENCILLA PASANDO LA URL SIMPLEMENTE'''

import webbrowser

def obtener_clima(ciudad):
    url = f'https://wttr.in/{ciudad}'
    webbrowser.open(url)
