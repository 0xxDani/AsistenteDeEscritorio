# IMPORTACIONES DE LIBRERÍAS
from dotenv import load_dotenv
from PyQt5.QtCore import QThread, pyqtSignal
import os
import pyjokes
import webbrowser
import speech_recognition as sr
import openai
import time
import pywhatkit
import datetime

# IMPORTACIONES DE ARCHIVOS ARCHIVOS
from weather import obtener_clima
from bd import editDataBase, editTable, EditColumn, InsertData
from abrirProgramaspc import abrir_programa
from speech import transformar_audio_a_texto, hablar
from mostrarDb import mostrar
from write import escribir_en_programa

# Carga las variables de entorno desde el archivo .env
load_dotenv('.env')
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Clase del Hilo del Asistente
class AssistantThread(QThread):
    # Señales para comunicar el estado del asistente
    assistant_started = pyqtSignal()
    assistant_stopped = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = False

    def start_assistant(self):
        # Inicia el asistente y la conversación.
        self.running = True
        self.conversation = ""                               # Se inicializa la conversación vacía.
        hablar("¿Qué necesitas?")                            # El asistente comienza saludando y esperando instrucciones.
        while self.running:
            question = transformar_audio_a_texto().lower()   # Se captura el audio y se transforma a texto y a minúscula.
            if question == "sigo esperando":
                continue                                     # Si no se detecta una pregunta, el asistente seguirá esperando.

            # Se registra la pregunta en la conversación.
            self.conversation += "\nTú: " + question + "\nSalo: "
            response = self.process_input(question)          # Procesar la pregunta y obtener la respuesta del asistente.
            answer = response.strip()                        # Se obtiene la respuesta sin espacios en blanco innecesarios.

            # Se registra la respuesta en la conversación.
            self.conversation += answer
            print("Salo: " + answer + "\n")                  # Imprimir la respuesta del asistente en la consola.
            
            if answer:
                hablar(answer)                               # Si hay una respuesta válida, el asistente la pronunciará.
            else:
                hablar("Repite nuevamente la solicitud mor") # Si no hay respuesta, el asistente pedirá que se repita la solicitud.
            time.sleep(0.3)                                  # Se añade una pequeña pausa entre interacciones para evitar problemas de audio.

    def process_input(self, question):
        # Se realizan algunas acciones específicas si el usuario solicita escribir en programas de texto.
        # Luego, si no se encuentra una acción específica, se utiliza la API de OpenAI para obtener una respuesta.
        # Se utiliza el modelo "text-davinci-003" para obtener la respuesta del asistente.

        if 'escribe en word' in question:
            texto = question.replace('escribe en word','').strip()
            escribir_en_programa(texto, 'word')
            return "Escribiendo en Word..."

        if 'escribir en wordpad' in question:
            texto = question.replace('escribir en wordpad', '').strip()
            escribir_en_programa(texto, 'wordpad')
            return "Escribiendo en WordPad..."

        if 'escribe en notepad' in question:
            texto = question.replace('escribe en notepad', '').strip()
            escribir_en_programa(texto, 'notepad')
            return "Escribiendo en el Bloc de notas..."

        if question.startswith('abre') or question.startswith('ejecuta') or question.startswith('abre el') or question.startswith('ejecuta el') or question.startswith('ejecuta la') or question.startswith('abrir'):
            programa = question.replace('abre', '').replace('ejecuta', '').replace('la', '').replace('abrir', '').strip()
            abrir_programa(programa)
            return f"Abriendo {programa}..."


        if 'reproduce' in question:
            # Función para reproducir música y videos en YouTube
            music = question.replace('reproduce', '').strip()
            pywhatkit.playonyt(music)
            return "Reproduciendo " + music

        if 'dime la hora actual' in question:
            # Función para obtener la hora actual
            hora = datetime.datetime.now().strftime('%I:%M %p')
            return "Son las " + hora

        if 'dime la fecha actual' in question:
            # Función para obtener la fecha actual
            fecha = datetime.datetime.now().strftime('%d/%m/%Y')
            return "Hoy es " + fecha
        
        if 'clima' in question:
            ciudad = question.replace('clima', '').strip()
            obtener_clima(ciudad)
            return "Mostrando información del clima para {}".format(ciudad)


        if 'busca' in question:
            # Función para realizar una búsqueda en Internet
            order = question.replace('busca', '').strip()
            pywhatkit.search(order)
            return "Buscando " + order

        if 'dime un chiste' in question:
            # Función para contar un chiste
            return pyjokes.get_joke('es')

        if 'crea la carpeta' in question:
            # Función para crear una carpeta en el PC
            home = "C:\\tu ruta\\Tu ruta\\Desktop\\Asistente\\" #AQUÍ DEBES ACOMODAR TU RUTA DEL PROYECTO O LA RUTA QUE QUIERAS
            order = question.replace('crea la carpeta', '').strip()
            if os.path.exists(order):
                return "La carpeta ya existe"
            else:
                os.mkdir(home + order)
                return "La carpeta se creó correctamente"

        if 'elimina la carpeta' in question:
            # Función para eliminar un directorio en el PC
            home = "C:\\tu ruta\\Tu ruta\\Desktop\\Asistente\\"   #AQUÍ DEBES ACOMODAR TU RUTA DEL PROYECTO O LA RUTA QUE QUIERAS
            order = question.replace('borra el directorio', '').strip()
            full_path = os.path.join(home, order)
            if os.path.exists(full_path):
                os.rmdir(full_path)
                return "Se eliminó el directorio correctamente"
            else:
                return "El directorio no existe"

        if 'crea el archivo' in question:
            # Función para crear un archivo de texto
            order = question.replace('crea el archivo', '').strip()
            order = order + '.txt'
            if os.path.exists(order):
                return "El archivo ya existe"
            else:
                archivo = open(order, "w")
                archivo.close()
                return "Se creó el archivo correctamente"

        if 'elimina el archivo' in question:
            # Función para eliminar un archivo de texto
            order = question.replace('elimina el archivo', '').strip()
            order = order + '.txt'
            if os.path.exists(order):
                os.remove(order)
                return "Se eliminó el archivo correctamente"
            else:
                return "El archivo no existe"

            #BASES DE DATOS**********************************************************************
        if 'crea la base de datos' in question:
            name = question.replace('crea la base de datos', '').strip()
            editDataBase(name, True)
            return "Base de datos {} creada correctamente".format(name)

        if 'edita la base de datos' in question:
            order = question.replace('edita la base de datos', '').strip()
            dataname = order.strip()

            hablar('Que desea editar en la base de datos '+dataname+'?')
            rec = transformar_audio_a_texto()

            if 'crear la tabla' in rec:
                order = rec.replace('crear la tabla', '').strip()
                tablename = order.strip()
                editTable(dataname, tablename, True)
                return "Tabla {} creada correctamente en la base de datos {}".format(tablename, dataname)

            elif 'editar la tabla' in rec:
                tablename = rec.replace('editar la tabla', '').strip()
                tablename = tablename.strip()
                EditColumn(dataname, tablename)

            elif 'insertar datos en la tabla' in rec:
                tablename = rec.replace('insertar datos en la tabla', '').strip()
                tablename = tablename.strip()
                InsertData(dataname, tablename)
                return 

            elif 'eliminar la tabla' in rec:
                tablename = rec.replace('eliminar la tabla', '').strip()
                tablename = tablename.strip()
                editTable(dataname, tablename, False)
                return "Tabla {} eliminada correctamente de la base de datos {}".format(tablename, dataname)

        if 'eliminar la base de datos' in question:
            name = question.replace('eliminar la base de datos', '').strip()
            editDataBase(name, False)
            return "Base de datos {} eliminada correctamente".format(name)

        if 'mostrar la base de datos' in question:
            # Función para mostrar tablas en la base de datos
            database = question.replace('mostrar la base de datos', '').strip()
            mostrar(database)
            self.running = False
            return '' 

        if 'satoshi' in question:
            # Función para redirigir a un sitio web específico
            webbrowser.open('https://coinmarketcap.com/currencies/green-satoshi-token-bsc/')
            return "Redireccionando a Satoshi"
        
        if 'bitcoin' in question:
            # Función para redirigir a la página de Bitcoin en CoinMarketCap
            webbrowser.open('https://coinmarketcap.com/currencies/bitcoin/')
            return "Redireccionando a Bitcoin"

        if 'ethereum' in question:
            # Función para redirigir a la página de Bitcoin en CoinMarketCap
            webbrowser.open('https://coinmarketcap.com/currencies/ethereum/')
            return "Redireccionando a Ethereum"

        if 'cardano' in question:
            webbrowser.open('https://www.gmail.com/')
            return "Redireccionando gmail"

        if 'tradingview' in question:
            webbrowser.open('https://es.tradingview.com/')
            return "Redireccionando a trading view"

        if 'emisoras' in question:
            webbrowser.open('http://radio.garden/visit/altagracia/Gd1jaPa_')
            return "Redireccionando a radio garden"
        
        if 'google' in question:
            webbrowser.open('https://www.google.com/')
            return "Redireccionando a google"

        if 'youtube' in question:
            webbrowser.open('https://www.youtube.com/')
            return "Redireccionando a youtube"

        if 'gmail' in question:
            webbrowser.open('https://www.gmail.com/')
            return "Redireccionando gmail"

        if 'php my admin' in question:
            webbrowser.open('http://localhost/phpmyadmin/')
            return "Redireccionando a Phpmyadmin"

        #SE DEFINE EL MODELO CON EL QUE VA A TRABAJAR EL BOT EN ESTE CASO text-davinci-003
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.conversation,
            temperature=0.5,
            max_tokens=90,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["\n", " Tú:", " Salo:"]
        )
        return response.choices[0].text.strip()

    def stop_assistant(self):
        # Detiene el asistente y emite una señal de que se detuvo.
        self.running = False
        self.assistant_stopped.emit()

    def run(self):
        # Método principal del hilo. Inicia el asistente, emite una señal de inicio y detiene el asistente.
        self.assistant_started.emit()
        self.start_assistant()
        self.assistant_stopped.emit()