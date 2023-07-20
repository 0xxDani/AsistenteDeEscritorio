'''UN CRUD POR MEDIO DE VOZ, SE CREA, ELIMINA, INSERTAN Y SE MUESTRAN LOS DATOS DE LA BASE DE DATOS,
LA FUNCIÓN DE MOSTRAR SE PUSO APARTE...🦉'''

import speech_recognition as sr
import pymysql
from os import system
from speech import hablar, transformar_audio_a_texto


error='Conexion Fallida y error de sintaxis'

# Función para crear o eliminar una base de datos
def editDataBase(name,cond):
    # Conexión a la base de datos del sistema (MySQL).
    try:
        miconexion=pymysql.connect(host="localhost",user="your user",password="your password",db="mysql")
        micursor=miconexion.cursor()
        hablar('Conexion exitosa')

        if cond == True:
            #Creando base de datos
            micursor.execute("CREATE DATABASE IF NOT EXISTS "+name)
            hablar("Base de datos creada correctamente")
        
        elif cond == False:
            #Eliminando base de datos
            micursor.execute("DROP DATABASE "+name)
            hablar("Base de datos eliminada correctamente")

        #Cierre de conexion
        miconexion.commit()
        miconexion.close()
        micursor.close()

    except:
        hablar(error)

# Función para crear o eliminar una tabla dentro de una base de datos
def editTable(dataname, tablename, cond):
    try:
        #Ingresando a la base de datos "dataname"
        miconexion=pymysql.connect(host="localhost",user="your user",password="your password",db=dataname)
        micursor=miconexion.cursor()

        #Creando tablas en "dataname" y agregando una columna por defecto
        if cond == True:
            micursor.execute("CREATE TABLE IF NOT EXISTS " + tablename + " (defaultID INT(11) AUTO_INCREMENT, nombre_usuario VARCHAR(255), email VARCHAR(255), telefono VARCHAR(20), CONSTRAINT default_pk PRIMARY KEY (defaultID))")

            hablar( "Tabla {} editada correctamente en la base de datos {}".format(tablename, dataname))

        elif cond == False:
            # Eliminar tabla si "cond" es False.
            micursor.execute("DROP TABLE "+tablename)
            hablar("Tabla eliminada correctamente")

        #Cierre de conexion 
        miconexion.commit()
        miconexion.close()
        micursor.close()

    except:
        hablar(error)
    
# Función para agregar, modificar o eliminar una columna en una tabla de una base de datos
def EditColumn(dataname, tablename):
    try:
        #Ingresando a la base de datos "dataname"
        miconexion=pymysql.connect(host="localhost",user="your user",password="your password",db=dataname)
        micursor=miconexion.cursor()

        print('Opciones: crear columna, editar columna, eliminar columna')
        rec = transformar_audio_a_texto()
        system("cls")

        if 'crear columna' in rec:
            hablar('Por favor siga el siguiente formato')
            print('var_name var_type(var_long) extras')

            columnname = input('Valor: ')
            micursor.execute("ALTER TABLE "+tablename+" ADD ("+columnname+")")
            hablar('Columna creada correctamente')
            
        elif 'editar columna' in rec:
            print('Opciones: modificar columna, cambiar nombre')
            rec = transformar_audio_a_texto()

            if 'modificar columna' in rec:
                hablar('Por favor, ingrese los nuevos datos de la columna')
                print('Formato: var_name var_type(var_long) extras')

                newcolumn = input('Valor: ')
                micursor.execute("ALTER TABLE "+tablename+" MODIFY "+ newcolumn)
                hablar('Columna modificada correctamente')


            elif 'cambiar nombre' in rec:
                hablar('Ingrese la columna a renombrar: ')
                oldcolumn = input('Valor: ')
                system('cls')

                hablar('Por favor, ingrese los nuevos datos de la columna')
                print('Formato: var_name var_type(var_long) extras')

                newcolumn = input('Valor: ')

                micursor.execute("ALTER TABLE "+tablename+" CHANGE "+ oldcolumn + " " + newcolumn)
                hablar('Datos modificados con exito')              

        elif 'eliminar columna' in rec:
            hablar("Porfavor, ingrese la columna a eliminar")
            columnname = input("valor: ")
                                
            micursor.execute("ALTER TABLE "+tablename+" DROP "+columnname)
            hablar("Columna eliminada correctamente")

        #Cierre de conexion
        miconexion.commit()
        miconexion.close()
        micursor.close()

    except:
        hablar(error)


# Función para insertar datos en una tabla de una base de datos
def InsertData(dataname, tablename):
    try:
        #Ingresando a la base de datos "dataname"
        miconexion=pymysql.connect(host="localhost",user="your user",password="your password",db=dataname)
        micursor=miconexion.cursor()

        #Establecer columna en la que se ingresará el dato.
        hablar('Ingrese el nombre de la columna')
        columnname = input('Columna de la tabla donde desea ingresar el dato: ')

        #Datos en la columna
        hablar('Dato a ingresar en la columna: ')
        data = input('Dato a ingresar: ')

        # Consulta para insertar el dato en la columna.
        micursor.execute("insert into "+tablename+"("+columnname+")"+" values('{}')".format(data))
        hablar("Datos insertados correctamente en la tabla {} de la base de datos {}".format(tablename, dataname))
        
        #Cerrar conexion
        miconexion.commit()
        miconexion.close()
        micursor.close()

    except:
        hablar(error)
    