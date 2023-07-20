'''ESTE ARCHIVO SE ENCARGA DE LA VOZ Y CONVERTIRLA A TEXTO PARA GENERAR RESPUESTAS'''


import speech_recognition as sr       # Importar la biblioteca speech_recognition y renombrarla como "sr"
from gtts import gTTS                 # Importar la clase gTTS del módulo gtts
from pygame import mixer              # Importar el módulo mixer del paquete pygame
import random                         
import time    
import os  

def transformar_audio_a_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("Ya puedes hablar!")
        while True:
            audio = r.listen(origen)
            try:
                pedido = r.recognize_google(audio, language="es-AR")
                print("You: " + pedido)
                if pedido:
                    # Llamar a la función de procesamiento de la entrada del usuario aquí
                    break  # Salir del bucle cuando se recibe una entrada válida
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue
            except:
                continue
    return pedido

def hablar(mensaje):
    volume = 0.7                                         # Establecer el volumen para la reproducción del mensaje de voz
    tts = gTTS(mensaje, lang="es", slow=False)           # Crear una instancia de la clase gTTS para convertir el texto en voz
    ran = random.randint(0, 9999)                        # Generar un número aleatorio para el nombre del archivo de audio
    filename = 'Temp' + format(ran) + '.mp3'             # Crear el nombre del archivo de audio
    tts.save(filename)                                   # Guardar el archivo de audio con el mensaje de voz
    mixer.init()                                         # Inicializar el módulo mixer de pygame
    mixer.music.load(filename)                           # Cargar el archivo de audio
    mixer.music.set_volume(volume)                       # Establecer el volumen de reproducción
    mixer.music.play()                                   # Reproducir el mensaje de voz
    while mixer.music.get_busy():                        # Esperar hasta que la reproducción del mensaje de voz finalice
        time.sleep(0.5)
    mixer.quit()                                         # Detener el módulo mixer de pygame
    os.remove(filename)                                  # Eliminar el archivo de audio temporal
