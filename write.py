import pyautogui
import time
from abrirProgramaspc import abrir_programa
from difflib import SequenceMatcher

def escribir_en_programa(texto, programa):
    if verificar_palabra_clave(programa, 'word'):
        # Abre Word
        abrir_programa('word')

        # Espera un momento para asegurarse de que Word se haya abierto completamente
        time.sleep(3)

        # Mueve el cursor al inicio del programa
        pyautogui.hotkey('ctrl', 'home')

        # Pequeña pausa antes de la escritura
        time.sleep(0.5)

        # Escribe el texto en Word
        pyautogui.write(texto, interval=0.1)

    elif verificar_palabra_clave(programa, 'wordpad'):
        # Abre WordPad
        abrir_programa('wordpad')

        # Espera un momento para asegurarse de que WordPad se haya abierto completamente
        time.sleep(3)

        # Mueve el cursor al inicio del programa
        pyautogui.hotkey('ctrl', 'home')

        # Pequeña pausa antes de la escritura
        time.sleep(0.5)

        # Escribe el texto en WordPad
        pyautogui.write(texto, interval=0.1)

    elif verificar_palabra_clave(programa, 'notepad'):
        # Abre el Bloc de notas
        abrir_programa('notepad')

        # Espera un momento para asegurarse de que el Bloc de notas se haya abierto completamente
        time.sleep(3)

        # Mueve el cursor al inicio del programa
        pyautogui.hotkey('ctrl', 'home')

        # Pequeña pausa antes de la escritura
        time.sleep(0.5)

        # Escribe el texto en el Bloc de notas
        pyautogui.write(texto, interval=0.1)

    else:
        return "No se reconoce el programa especificado."

def verificar_palabra_clave(texto, palabra_clave):
    # Usar SequenceMatcher para comparar el texto con la palabra clave y obtener un ratio de similitud.
    ratio = SequenceMatcher(None, texto.lower(), palabra_clave).ratio()

    # Si el ratio de similitud es mayor o igual a 0.8, consideramos que la palabra clave se encuentra en el texto.
    if ratio >= 0.8:
        return True
    else:
        # Si el ratio de similitud es menor a 0.8, consideramos que la palabra clave no se encuentra en el texto.
        return False
