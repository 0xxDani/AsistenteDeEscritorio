'''AQUÍ HAY UNA ESTRUCTURA BÁSICA PARA MOSTRAR LAS BASES DE DATOS QUE SE TENGAN EN MYSQL, RECORDAR ASIGNAR
EL ROOT Y EL PASSWORD DE TU BASE DE DATOS🦉 '''


import speech_recognition as sr                         # LIBRERÍA PARA RECONOCIMIENTO DE VOZ
import pyttsx3                                          # LIBRERÍA PARA SÍNTESIS DE VOZ
import pywhatkit                                        # LIBRERÍA PARA REALIZAR ACCIONES CON COMANDOS
import pymysql                                          # LIBRERÍA PARA MANIPULAR DATOS DE MYSQL
import os                                               # LIBRERÍA PARA MANIPULAR DATOS DEL SISTEMA OPERATIVO
from os import system
from tkinter import *                                   #SE USA TK INTER PARA MOSTRAR UNA NUEVA VUENTANA PARA MOSTRAR LA DB.
from tkinter import ttk
from tkinter import Tk, ttk, Listbox, Scrollbar, END
import mysql.connector

from speech import transformar_audio_a_texto, hablar

error='Conexion Fallida y error de sintaxis'

def mostrar(database):
    try:
        # Establecer la conexión con la base de datos
        miConexion = mysql.connector.connect(user='your-user', password='your password', host='localhost', database=database)
        miCursor = miConexion.cursor()
        hablar("Mostrando tablas en la base de datos " + database)

        # Obtener los nombres de las tablas en la base de datos
        miCursor.execute("SHOW TABLES")
        tables = miCursor.fetchall()

        # Crear una ventana
        window = Tk()
        window.title("Tablas en la base de datos " + database)
        window.geometry('780x460')
        window.config(bg='#F2F2F2')

        # Función para actualizar el Treeview al hacer clic en una tabla de la lista
        def update_treeview(event):
            selected_table = listbox.get(ACTIVE)
            miCursor.execute(f"SELECT * FROM {selected_table}")
            rec = miCursor.fetchall()

            # Obtener los nombres de las columnas
            miCursor.execute(f"DESCRIBE {selected_table}")
            column_names = [column[0] for column in miCursor.fetchall()]

            # Limpiar el Treeview actual
            tree.delete(*tree.get_children())

            # Insertar los registros en el Treeview
            for record in rec:
                tree.insert("", END, values=record)  #'text=selected_table' aqui puedo poner esto para asignar un valor a las filas de la columna tabla

            # Actualizar las columnas en el Treeview
            tree["columns"] = tuple(column_names)
            for column_name in column_names:
                tree.column(column_name, width=130)
                tree.heading(column_name, text=column_name)

        # Crear un Listbox con scroll vertical para mostrar la lista de tablas
        listbox_frame = ttk.Frame(window)
        listbox_frame.pack(side="left", fill="y")

        scrollbar_y = Scrollbar(listbox_frame, orient="vertical")
        listbox = Listbox(listbox_frame, width=28, yscrollcommand=scrollbar_y.set)
        scrollbar_y.config(command=listbox.yview)
        scrollbar_y.pack(side="right", fill="y")
        listbox.pack(side="left", fill="y")

        # Insertar las tablas en el Listbox
        for table in tables:
            listbox.insert(END, table[0])

        # Asociar la función de actualización al evento de clic en el Listbox
        listbox.bind("<<ListboxSelect>>", update_treeview)

        # Crear un árbol con scroll horizontal y vertical para mostrar los datos
        tree_frame = ttk.Frame(window)
        tree_frame.pack(side="left", padx=5, fill="both", expand=FALSE)

        scrollbar_x = Scrollbar(tree_frame, orient="horizontal")
        scrollbar_y = Scrollbar(tree_frame, orient="vertical")
        tree = ttk.Treeview(tree_frame, height=20, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        tree.heading("#0", text="Tabla")
        tree.column("#0", width=80)
        scrollbar_x.config(command=tree.xview)
        scrollbar_y.config(command=tree.yview)
        scrollbar_x.pack(side="bottom", fill="x")
        scrollbar_y.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)

        window.mainloop()

        # Cerrar la conexión y el cursor
        miCursor.close()
        miConexion.close()

    except:
        hablar(error)