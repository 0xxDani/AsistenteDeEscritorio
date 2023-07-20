## ASISTENTE EN PYTHON

#### DESCRIPCIÓN

Este es un proyecto de asistente virtual desarrollado en Python. El asistente puede realizar tareas como responder preguntas matemáticas, buscar información en la web, interactuar con una base de datos MySQL y abrir programas en tu PC. A continuación, se detalla cómo configurar y ejecutar el asistente.

El archivo que se debe ejecutar preferiblemente en visual studio code es main.py. Al salir la ventana del asistente solo se presiona iniciar asistente y ya puedes interactuar con el. Cuando desees detenerlo puedes presionar nuevamente el botón.

#### INSTRUCCIONES DE CONFIGURACIÓN

#### 1- CREAR UN AMBIENTE VIRTUAL EN PYTHON  (CREAR UNA CONSOLA DENTRO DE LA CARPETA DEL PROYECTO O EN LA CONSOLA DE VISUAL STUDIO TAMBIÉN FUNCIONA BIEN SIN PROBLEMA)

-         python -m venv venv

#### 2- ACTIVAR EL AMBIENTE VIRTUAL

-         venv\Scripts\activate

#### 3- INSTALAR LAS LIBRERÍAS DEL PROYECTO

-         pip install -r requirements.txt

#### 4- EN EL ARCHIVO .env SI DESEAS AGREGAS LA API DE OPENAI PARA OBTENER RESPUESTAS MATEMÁTICAS INTELIGENTES Y ALGUNAS OTRAS RESPUESTAS.

#### 5- DEBES MODIFICAR LOS ARCHIVOS bd, Y PONER TU ROOT Y PASSWORD PARA LA FUNCIÓN DE BASE DE DATOS EN MYSQL EN DONDE TE ENCUENTRE ESTA LINEA: 

       miConexion = mysql.connector.connect(user='your user', password='your password', host='localhost', database=database)

#### 6- EN EL ARCHIVO assistant_thread.py...PARA LA FUNCIÓN DE CREAR CARPETAS Y ARCHIVOS SE DEBEN AGREGAR LAS RUTAS EN DONDE SE QUIEREN CREAR LOS ARCHIVOS, MODIFICAR ESTALINEA DONDE LA ENCUENTRES:

      home = "C:\\tu ruta\\Tu ruta\\Desktop\\Asistente\\"

#### 7- EN LA FUNCION abrirProgramaspc DEBES AGREGAR LAS RUTAS EN DONDE SE ENCUENTRAN TUS PROGRAMAS, QUIZÁS ALGUNAS DE LAS QUE HAY FUNCIONAN POR DEFECTO PERO NO TODAS FUNCIONARÁN, PARA BUSCAR LA RUTA DE TUS ARCHIVOS.EXE DE FORMA SENCILLA SIGUE ESTOS PASOS:

- ABRIR EL ADMINISTRADOR DE TAREAS

- IR A LA PESTAÑA DETALLES

- ABRIR EL PROGRAMA QUE SE QUIERE UBICAR

- INMEDIATAMENTE SE ABRA EL PROGRAMA EL CUAL SE QUIERE BUSCAR EN LA PESTAÑA DETALLES EN LA COLUMNA DESCRIPCIÓN, DEBE ESTAR EL PROGRAMA EN EJECUCIÓN O SE PUEDE BUSCAR EN LA LUPA(BUSCADOR)

- SE DA CLICK DERECHO, ABRIR UBICACIÓN DEL ARCHIVO, ESTO TE LLEVARÁ A LA CARPETA DONDE SE ENCUENTRE EL .EXE.

- LUEGO EN EL ARCHIVO SE DA CLICK DERECHO Y COPIAR RUTA DE ACCESO....

- ESA RUTA SE PEGA ALLA EN LA FUNCIÓN ABRIR PROGRAMAS, ACOMODANDOLA DENTRO DEL DICCIONARIO 'programas' USANDO LA SINTAXIS QUE TIENE CON LAS DOBLES BARRAS INVERTIDAS. EJEMPLO.

-    "navegador": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk",



##### NOTA: SI EN CASO TAL LA LIBRERÍA 'dotenv' PRESENTA LÍOS PARA INSTALAR, UTILIZAR ESTE COMANDO ADICIONAL EN LA CONSOLA:
-      python -m pip install python-dotenv


### FUNCIONES DEL ASISTENTE.

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
      *insertar datos en la tabla...'''

###### CREADOR: DANIEL BUSTAMANTE O. 🦉🖤20/07/2023🖤🦉
###### CONTACTO: 0xsnake55@gmail.com
