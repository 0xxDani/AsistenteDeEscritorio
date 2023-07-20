import os

#AQUI DEBES DEFINIR TUS RUTAS EN DONDE ESTÉN TUS ARCHIVOS...¿NO SABES COMO UBICARLAS?...VER README.me
def abrir_programa(programa):
# Definir el diccionario de programas y rutas
    programas = {
    "navegador": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk",
    "navegador edge": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk",
    "navegador chrome": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk",
    "navegador firefox": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk",
    "wordpad": "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe",
    "calcudora": "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCalculator_11.2210.0.0_x64__8wekyb3d8bbwe\\CalculatorApp.exe",
    "paint": "C:\\Program Files\\WindowsApps\\Microsoft.Paint_11.2302.19.0_x64__8wekyb3d8bbwe\\PaintApp\\mspaint.exe",
    "word": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk",
    "access": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access.lnk",
    "powerpoint": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk",
    "one drive": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneDrive.lnk",
    "servidor": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\XAMPP\\XAMPP Control Panel.lnk",
    "winrar": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\WinRAR\\WinRAR.lnk",
    "windows powershl": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell ISE (x86).lnk",
    "android studio": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio\\Android Studio.lnk",
    "anaconda": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator.lnk",
    "netbeans": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Apache NetBeans\\Apache NetBeans IDE 16.lnk",
    "aragón": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Laragon\\Laragon.lnk",
    "avast": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Avast Premium Security.lnk",
    "intligent": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\IntelliJ IDEA Community Edition 2021.3.3.lnk",  
    "app store": "C:\\Program Files\\WindowsApps\\Microsoft.WindowsStore_22306.1401.1.0_x64__8wekyb3d8bbwe\\WinStore.App.exe",
    "cortana": "C:\\Program Files\\WindowsApps\\Microsoft.549981C3F5F10_4.2204.13303.0_x64__8wekyb3d8bbwe\\Cortana.exe",
    "fotos": "C:\\Program Files\\WindowsApps\\Microsoft.Windows.Photos_2023.11050.16005.0_x64__8wekyb3d8bbwe\\PhotosApp.exe",
    "roj": "C:\\Program Files\\WindowsApps\\Microsoft.WindowsAlarms_11.2304.0.0_x64__8wekyb3d8bbwe\\Time.exe",
    "voice access": "C:\\Windows\\System32\\VoiceAccess.exe",
    "lupa": "C:\\Windows\\System32\\Magnify.exe",
    "herramienta de recortes": "C:\\Program Files\\WindowsApps\\Microsoft.ScreenSketch_11.2304.21.0_x64__8wekyb3d8bbwe\\SnippingTool\\SnippingTool.exe",    "grabadora de sonido": "C:\\Program Files\\WindowsApps\\Microsoft.WindowsSoundRecorder_11.2304.25.0_x64__8wekyb3d8bbwe\\VoiceRecorder.exe",#se demora 
    "data browser": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\DB Browser (SQLite).lnk",
}

    if programa in programas:
        ruta_programa = programas[programa]
        # Se tiliza 'os.startfile' para abrir el programa en la ruta especificada.
        os.startfile(ruta_programa)
        print(f"Abriendo {programa}...")
    else:
        print("No se encontró el programa especificado.")

