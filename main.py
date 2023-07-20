from PyQt5.QtGui import QColor, QPalette, QFont, QCursor, QMovie, QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea, QGridLayout, QApplication
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from qtmodern.styles import dark
import sys

'''Este archivo representa la ventana de la aplicación del asistente. Se crea una interfaz de usuario simple con un botón para iniciar/detener el asistente, una etiqueta de estado y una animación (imagen) del asistente. Cuando se hace clic en el botón "Iniciar Asistente", se inicia un hilo (AssistantThread) para ejecutar el asistente virtual, lo que permite que la interfaz gráfica siga siendo interactiva y no se bloquee durante la ejecución del asistente.

Para ejecutar esta aplicación, se llama a la función main() que crea una instancia de QApplication y muestra la ventana principal. La llamada a dark(app) aplica un tema oscuro (proporcionado por qtmodern) a la aplicación.'''

'''FORMAS DE COMUNICARSE CON SALO
   SIMPLEMENTE DECIR LA FRASE MÁGICA....EJEMPLO:
   Escribe en word, clima, crea la carpeta...etc...

    FUNCIONES DEL ASISTENTE.
      *Escribe en word
      *Escribir en wordpad
      *Escribe en notepad
      *Abre word...(o cualquier programa que se tenga ruteado)..tambien funciona con:
      -Abrir...
      -Abre el...
      -Ejecuta...
      -Ejecuta el...

      *reproduce...y el nombre de algun video en youtube

      *dime la hora actual
      *dime la fecha actual
      *clima

      *busca...y seguido di algo que quieras buscar en la web...

      *dime un chiste
      
      *crea la carpeta
      *elimina la carpeta
      *crea el archivo
      *elimina el archivo
      *emisoras
      *google
      *youtube
      *gmail
      *php my admin

      *crea la base de datos...  
      *eliminar la base de datos...
      *edita la base de datos...
      *crear la tabla...
      *eliminar la tabla...
      *editar la tabla...
      *crear columna:
                    NOTA: SIMPLEMENTE SE DEBEN COLOCAR LOS VALORES QUE QUEREMOS  CREAR O MODIFICAR ASI DE ESTA FORMA EN LA ESTRUCTURA DE LA COLUMNA
                    { Formato para crear columnas:  Nom_Estudiante VARCHAR(30) NOT NULL  }
      *editar columna 
                    { Formato para editar columnas:  nombre_usuario VARCHAR(300) NULL}
      *cambiar nombre 
                    { Formato para editar columnas:  nombre_usuario VARCHAR(300) NULL}
      *eliminar columna
      *insertar datos en la tabla...
      '''

# Importar el módulo AssistantThread desde el archivo assistant_thread.py
from assistant_thread import AssistantThread

# Definición de la clase principal de la ventana de asistente
class AssistantWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Variables para el hilo del asistente y estado del asistente
        self.assistant_thread = None
        self.assistant_running = False
        
        # Creación del diseño de la ventana principal
        layout = QVBoxLayout()

        # Botón para iniciar/detener el asistente
        self.start_button = QPushButton("Iniciar Asistente")
        self.start_button.clicked.connect(self.toggle_assistant)
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))

        # Etiqueta de estado del asistente
        self.status_label = QLabel("Esperando...")
        self.status_label.setAlignment(Qt.AlignCenter)

        # Creación de un área de desplazamiento
        scroll_area = QScrollArea()   #HAY COSITAS AQUÍ QUE ME FALTA AÑADIR HOHOH🦉
        scroll_area.setWidgetResizable(True)

        # Creación del widget de desplazamiento y diseño
        scroll_widget = QWidget()
        scroll_layout = QGridLayout(scroll_widget)
        scroll_layout.addWidget(self.start_button, 4, 0, alignment=Qt.AlignCenter)
        scroll_layout.addWidget(self.status_label, 5, 0, alignment=Qt.AlignCenter)

        # Etiqueta para mostrar una animación o imagen del asistente
        self.image_label = QLabel()
        self.movie = QMovie("img/S.gif")
        self.image_label.setMovie(self.movie)
        self.movie.start()

        scroll_layout.addWidget(self.image_label, 2, 0, alignment=Qt.AlignCenter)

        scroll_layout.setRowStretch(4, 1)
        scroll_area.setWidget(scroll_widget)

        layout.addWidget(scroll_area)

        self.setLayout(layout)

        # Estilos CSS para personalizar la apariencia de la ventana y widgets
        self.setWindowTitle("SALO ASISTENTE 🦉")
        self.setMinimumSize(538, 578)

        self.setStyleSheet("""
QWidget {
    background-color:  #0B0512;
}

QPushButton {
    background-color: #1F2540;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 20px;
    padding: 0px 0px;
    height: 50px;
    width: 170px;
    margin-top: 10px;
    border: 1px solid rgba(255, 255, 255, 0.5);
}

QPushButton:hover {
    background-color: #3A4A6B;
}

QLabel {
    color: white;
    font-size: 14px;
    margin-top: 10px;
}""")

    # Función para cambiar el estado del asistente (iniciar/detener)
    def toggle_assistant(self):
        if self.assistant_running:
            self.stop_assistant()
        else:
            self.start_assistant()

    # Función para iniciar el asistente y el hilo del asistente
    def start_assistant(self):
        self.start_button.setEnabled(False)
        self.start_button.setText("Iniciando...")
        self.assistant_running = True
        self.assistant_thread = AssistantThread(self)
        self.assistant_thread.assistant_started.connect(self.assistant_started)
        self.assistant_thread.assistant_stopped.connect(self.assistant_stopped)
        self.assistant_thread.start()

    # Función para detener el asistente y el hilo del asistente
    def stop_assistant(self):
        self.start_button.setEnabled(False)
        self.start_button.setText("Deteniendo...")
        self.assistant_thread.stop_assistant()

    # Función para manejar el evento de inicio del asistente
    def assistant_started(self):
        self.start_button.setEnabled(True)
        self.start_button.setText("Detener Asistente")
        self.status_label.setText("Asistente en ejecución")

    # Función principal que inicia la aplicación
    def assistant_stopped(self):
        self.start_button.setEnabled(True)
        self.start_button.setText("Iniciar Asistente")
        self.status_label.setText("Programa detenido")
        self.assistant_running = False

        # Habilitar el botón "Iniciar Asistente"
        self.start_button.setEnabled(True)

# Aplicar un tema oscuro a la aplicación
def main():
    app = QApplication(sys.argv)
    window = AssistantWindow()
    dark(app)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
